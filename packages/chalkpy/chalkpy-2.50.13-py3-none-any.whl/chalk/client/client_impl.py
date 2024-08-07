from __future__ import annotations

import base64
import collections.abc
import itertools
import json
import math
import os
import random
import re
import string
import subprocess
import time
import traceback
import uuid
from concurrent.futures import Future, ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from io import BytesIO
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Literal,
    Mapping,
    NoReturn,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
    overload,
)
from urllib.parse import urljoin

import pandas as pd
import pyarrow.feather
import requests
import urllib3.exceptions
from dateutil import parser
from requests import HTTPError
from requests import JSONDecodeError as RequestsJSONDecodeError
from requests.adapters import HTTPAdapter
from requests.models import ConnectionError
from tqdm import tqdm
from typing_extensions import override
from urllib3 import Retry

import chalk._repr.utils as repr_utils
from chalk._reporting.models import BatchReport, BatchReportResponse
from chalk._reporting.progress import ProgressService
from chalk._upload_features.utils import to_multi_upload_inputs
from chalk._version import __version__ as chalkpy_version
from chalk.client._internal_models.models import INDEX_COL_NAME, TS_COL_NAME, OfflineQueryGivensVersion
from chalk.client.client import ChalkClient
from chalk.client.dataset import DatasetImpl, DatasetRevisionImpl, DatasetVersion, dataset_from_response, load_dataset
from chalk.client.exc import CHALK_TRACE_ID_KEY, ChalkAuthException, ChalkBaseException, ChalkCustomException
from chalk.client.models import (
    BranchDeployRequest,
    BranchDeployResponse,
    BranchIdParam,
    BulkOnlineQueryResponse,
    BulkOnlineQueryResult,
    ChalkError,
    ChalkException,
    ComputeResolverOutputRequest,
    ComputeResolverOutputResponse,
    CreateOfflineQueryJobRequest,
    CreateOfflineQueryJobResponse,
    DatasetJobStatusRequest,
    DatasetResponse,
    DatasetRevisionPreviewResponse,
    DatasetRevisionSummaryResponse,
    ErrorCode,
    ExchangeCredentialsRequest,
    ExchangeCredentialsResponse,
    FeatureDropRequest,
    FeatureDropResponse,
    FeatureObservationDeletionRequest,
    FeatureObservationDeletionResponse,
    FeatureResult,
    FeatureStatisticsResponse,
    GetIncrementalProgressResponse,
    GetOfflineQueryJobResponse,
    IngestDatasetRequest,
    MultiUploadFeaturesRequest,
    MultiUploadFeaturesResponse,
    OfflineQueryContext,
    OfflineQueryInput,
    OfflineQueryParquetUploadURLResponse,
    OnlineQuery,
    OnlineQueryContext,
    OnlineQueryManyRequest,
    OnlineQueryRequest,
    OnlineQueryResponse,
    OnlineQueryResponseFeather,
    OnlineQueryResultFeather,
    PersistenceSettings,
    PlanQueryRequest,
    PlanQueryResponse,
    QueryMeta,
    ResolverReplayResponse,
    ResolverRunResponse,
    ResourceRequests,
    SetIncrementalProgressRequest,
    StreamResolverTestMessagePayload,
    StreamResolverTestRequest,
    StreamResolverTestResponse,
    TriggerResolverRunRequest,
    UpdateGraphEntityResponse,
    UploadedParquetShardedOfflineQueryInput,
    UploadFeaturesRequest,
    UploadFeaturesResponse,
    WhoAmIResponse,
)
from chalk.client.response import Dataset, FeatureReference, OnlineQueryResult
from chalk.client.serialization.query_serialization import MULTI_QUERY_MAGIC_STR, write_query_to_buffer
from chalk.config.auth_config import load_token
from chalk.config.project_config import load_project_config
from chalk.features import DataFrame, Feature, FeatureNotFoundException, FeatureWrapper, ensure_feature, unwrap_feature
from chalk.features._encoding.inputs import recursive_encode_inputs
from chalk.features._encoding.json import FeatureEncodingOptions
from chalk.features._encoding.outputs import encode_outputs
from chalk.features.feature_set import is_feature_set_class
from chalk.features.pseudofeatures import CHALK_TS_FEATURE
from chalk.features.resolver import Resolver
from chalk.features.tag import BranchId, DeploymentId, EnvironmentId
from chalk.importer import CHALK_IMPORT_FLAG
from chalk.parsed.branch_state import BranchGraphSummary
from chalk.utils import notebook
from chalk.utils.df_utils import pa_table_to_pl_df
from chalk.utils.log_with_context import get_logger
from chalk.utils.missing_dependency import missing_dependency_exception

if TYPE_CHECKING:
    import polars as pl
    import pyarrow as pa
    from pydantic import BaseModel, ValidationError

    QueryInput = Union[Mapping[FeatureReference, Any], pd.DataFrame, pl.DataFrame, DataFrame]
    QueryInputTime = Union[Sequence[datetime], datetime, None]
else:
    try:
        from pydantic.v1 import BaseModel, ValidationError
    except ImportError:
        from pydantic import BaseModel, ValidationError

_logger = get_logger(__name__)

T = TypeVar("T")


class _ChalkHTTPException(BaseModel):
    detail: str
    trace: Optional[str] = None
    errors: Optional[List[ChalkError]] = None


class _ChalkClientConfig(BaseModel):
    name: str
    client_id: str
    client_secret: str
    api_server: str
    query_server: str
    active_environment: Optional[str] = None
    branch: Optional[BranchId] = None
    preview_deployment_id: Optional[DeploymentId] = None


class _BranchDeploymentInfo(BaseModel):
    deployment_id: str
    created_at: datetime


class _BranchInfo(BaseModel):
    name: str
    latest_deployment: Optional[str]
    latest_deployment_time: Optional[datetime]
    deployments: List[_BranchDeploymentInfo]


class _BranchMetadataResponse(BaseModel):
    branches: List[_BranchInfo]

    def __str__(self):
        def _make_line(info: _BranchInfo) -> str:
            latest_str = ""
            if info.latest_deployment_time and info.latest_deployment_time:
                latest_str = f" -- latest: {info.latest_deployment_time.isoformat()} ({info.latest_deployment})"
            return f"* `{info.name}`:\t{len(info.deployments)} deployments" + latest_str

        return "\n".join(_make_line(bi) for bi in self.branches)


def _validate_offline_query_inputs(
    inputs: Mapping[Union[str, Feature, Any], Any]
) -> Mapping[Union[str, Feature, Any], Any]:
    if len(inputs) == 0:
        return inputs

    def _is_scalar(v: Any):
        return not isinstance(v, collections.abc.Iterable) or isinstance(v, str)

    scalar_values = {k: v for (k, v) in inputs.items() if _is_scalar(v)}
    if len(scalar_values) == len(inputs):
        return {str(k): [v] for (k, v) in inputs.items()}
    elif len(scalar_values) > 0:
        first_key = next(iter(scalar_values.keys()))
        error_msg = (
            f"Failed to parse query inputs: offline_query() expects multiple input values for each feature. "
            f"Found a single value of type {type(inputs[first_key])} for key '{str(first_key)}'."
        )
        raise ValueError(error_msg)
    else:
        return {str(k): v for (k, v) in inputs.items()}


def _offline_query_inputs_to_parquet(
    offline_query_inputs: Sequence[OfflineQueryInput],
) -> List[pa.Table]:
    """
    Convert a list of OfflineQueryInput objects to a list of pyarrow Tables in the format
    OfflineQueryGivensVersion.SINGLE_TS_COL_NAME_WITH_URI_PREFIX
    """
    try:
        import pyarrow as pa
    except ImportError:
        raise missing_dependency_exception("chalkpy[runtime]")
    offset = 0
    tables = []
    for single_input in offline_query_inputs:
        pa_arrays: dict[str, pa.Array | pa.ChunkedArray] = {}
        for column_name, values in zip(single_input.columns, single_input.values):
            normalized_column_name = TS_COL_NAME if column_name == str(CHALK_TS_FEATURE) else column_name
            try:
                feature = Feature.from_root_fqn(column_name)
            except FeatureNotFoundException:
                pa_arrays[normalized_column_name] = pa.array(values)
            else:
                pa_arrays[normalized_column_name] = feature.converter.from_json_to_pyarrow(values)
        array_lengths = {len(v) for v in pa_arrays.values()}
        if len(array_lengths) != 1:
            raise ValueError(
                f"Failed to convert offline query input to parquet: "
                + f"all columns must have the same number of values, but found {array_lengths}"
            )
        (chunk_length,) = array_lengths
        pa_arrays[INDEX_COL_NAME] = pa.array(range(offset, offset + chunk_length), type=pa.int64())
        offset += chunk_length
        tables.append(pa.Table.from_pydict(pa_arrays))
    return tables


def _to_offline_query_input(
    input: QueryInput,
    input_times: QueryInputTime,
) -> OfflineQueryInput:
    try:
        import polars as pl
    except ImportError:
        raise missing_dependency_exception("chalkpy[runtime]")
    if isinstance(input, (DataFrame, pl.DataFrame)):
        input = input.to_pandas()
    if isinstance(input, collections.abc.Mapping):
        input = _validate_offline_query_inputs(input)
    pd_dataframe: pd.DataFrame
    if isinstance(input, pd.DataFrame):
        pd_dataframe = input
    else:
        pd_dataframe = pd.DataFrame(cast(Any, input))

    columns = pd_dataframe.columns
    matrix: List[List[Any]] = pd_dataframe.T.values.tolist()

    columns_fqn = [str(c) for c in (*columns, CHALK_TS_FEATURE)]
    if input_times is None:
        input_times = datetime.now(timezone.utc)
    if isinstance(input_times, datetime):
        input_times = [input_times for _ in range(len(pd_dataframe))]
    local_tz = datetime.now(timezone.utc).astimezone().tzinfo

    input_times = [x.replace(tzinfo=local_tz) if x.tzinfo is None else x for x in input_times]
    input_times = [x.astimezone(timezone.utc) for x in input_times]

    matrix.append([a for a in input_times])

    for col_index, column in enumerate(matrix):
        for row_index, value in enumerate(column):
            try:
                f = Feature.from_root_fqn(columns_fqn[col_index])
            except FeatureNotFoundException:
                # The feature is not in the graph, so passing the value as-is and hoping it's possible
                # to json-serialize it
                encoded_feature = value
            else:
                encoded_feature = f.converter.from_rich_to_json(
                    value,
                    missing_value_strategy="error",
                )

            matrix[col_index][row_index] = encoded_feature

    return OfflineQueryInput(
        columns=columns_fqn,
        values=matrix,
    )


def _upload_table_parquet(
    table: pa.Table,
    url: str,
) -> None:
    try:
        import pyarrow.parquet as pq
    except ImportError:
        raise missing_dependency_exception("chalkpy[runtime]")
    written_bytes = BytesIO()
    pq.write_table(table, written_bytes)
    written_bytes.seek(0)
    resp = requests.put(url, data=written_bytes)
    resp.raise_for_status()


def _convert_datetime_param(
    param_name: Literal["lower_bound", "upper_bound"], param: datetime | str | None
) -> datetime | None:
    """Takes an API parameter representing an optional datetime value and converts it into a datetime object."""
    if param is None:
        return None

    if isinstance(param, str):
        # Note: If the ISO 8601 string doesn't contain a timezone, we assume the timezone is UTC.
        # This is different behavior from the original datetime param, which tries to infer the caller's local timezone.
        # Going forward, we want to always assume UTC when no timezone is provided.
        # However, to maintain backwards compatibility, datetime-type params will continue to infer local timezone.
        try:
            param = datetime.fromisoformat(param)
        except ValueError:
            raise ValueError(
                f'Passed {param_name}="{param}", but {param_name} expects a datetime string in ISO 8601 format.'
            )

        if param.tzinfo is None:
            # Don't convert the datetime object with "astimezone", just slap on UTC timezone without changing the numbers
            return param.replace(tzinfo=timezone.utc)
        return param
    elif param.tzinfo is None:
        # Infer local timezone when the parameter is passed as a datetime object with no timezone
        return param.astimezone()

    return param


class OnlineQueryResponseImpl(OnlineQueryResult):
    data: List[FeatureResult]
    warnings: List[str]
    meta: Optional[QueryMeta]

    def __init__(
        self,
        data: List[FeatureResult],
        errors: List[ChalkError],
        warnings: List[str],
        meta: Optional[QueryMeta] = None,
    ):
        super().__init__()
        self.data = data
        self.errors = errors
        self.warnings = warnings
        self.meta = meta

        for d in self.data:
            if isinstance(d.value, float) and math.isnan(d.value):
                d.value = None
            if d.value is not None:
                try:
                    f = Feature.from_root_fqn(d.field)
                except FeatureNotFoundException:
                    self.warnings.append(
                        f"Return data {d.field}:{d.value} cannot be decoded. Attempting to JSON decode"
                    )
                else:
                    if f.is_has_many:
                        # Has-manys are returned by the server in a columnar format, i.e.:
                        # {"columns": ["book.id", "book.title"], "values": [[1, 2], ["Dune", "Children of Dune"]]}
                        # FeatureConverter expects a list of structs, i.e.:
                        # [{"book.id": 1, "book.title": "Dune"}, {"book.id": 2, "book.title": "Children of Dune"}]
                        assert isinstance(d.value, dict)
                        cols = d.value["columns"]
                        vals = d.value["values"]
                        vals_flattened = list(zip(*vals))
                        d.value = f.converter.from_json_to_rich(
                            [{k: v for k, v in zip(cols, row)} for row in vals_flattened]
                        )
                    elif f.is_has_many_subfeature:
                        # TODO we might need mulitple levels of nesting for has-many-has-many's
                        assert isinstance(d.value, collections.abc.Iterable)
                        d.value = [f.converter.from_json_to_rich(v) for v in d.value]
                    else:
                        d.value = f.converter.from_json_to_rich(d.value)

        self._values = {d.field: d for d in self.data}

    def _df_repr(self) -> List[Dict[str, Any]]:
        return [{"Feature": x.field, "Value": repr_utils.get_repr_value(x.value)} for x in self.data]

    def __repr__(self) -> str:
        lines = []
        for e in self.errors or []:
            nice_code = str(e.code.value).replace("_", " ").capitalize()
            # {str(e.category.value).capitalize()}
            lines.append(
                f"### {nice_code}{e.feature and f' ({e.feature})' or ''}{e.resolver and f' ({e.resolver})' or ''}"
            )
            lines.append(e.message)
            lines.append("")

            metadata = {
                "Exception Kind": e.exception and e.exception.kind,
                "Exception Message": e.exception and e.exception.message,
                "Stacktrace": e.exception and e.exception.stacktrace,
            }
            metadata = {k: v for k, v in metadata.items() if v is not None}
            for k, v in metadata.items():
                lines.append(f"*{k}*")
                lines.append("")
                lines.append(v)
        errs = "\n".join(lines)

        return repr(pd.DataFrame(self._df_repr())) + "\n" + errs

    def __str__(self):
        lines = []
        for e in self.errors or []:
            nice_code = str(e.code.value).replace("_", " ").capitalize()
            # {str(e.category.value).capitalize()}
            lines.append(
                f"### {nice_code}{e.feature and f' ({e.feature})' or ''}{e.resolver and f' ({e.resolver})' or ''}"
            )
            lines.append(e.message)
            lines.append("")

            metadata = {
                "Exception Kind": e.exception and e.exception.kind,
                "Exception Message": e.exception and e.exception.message,
                "Stacktrace": e.exception and e.exception.stacktrace,
            }
            metadata = {k: v for k, v in metadata.items() if v is not None}
            for k, v in metadata.items():
                lines.append(f"*{k}*")
                lines.append(f"")
                lines.append(v)
        errs = "\n".join(lines)
        return str(pd.DataFrame(self._df_repr())) + "\n" + errs

    def _repr_markdown_(self):
        lines = []
        if self.errors is not None and len(self.errors) > 0:
            lines.append(f"## {len(self.errors)} Errors")
            lines.append("")
            for e in self.errors:
                nice_code = str(e.code.value).replace("_", " ").capitalize()
                # {str(e.category.value).capitalize()}
                lines.append(
                    f"### {nice_code}{e.feature and f' ({e.feature})' or ''}{e.resolver and f' ({e.resolver})' or ''}"
                )
                lines.append(e.message)
                lines.append("")

                metadata = {
                    "Exception Kind": e.exception and e.exception.kind,
                    "Exception Message": e.exception and e.exception.message,
                    "Stacktrace": e.exception and e.exception.stacktrace,
                }
                metadata = {k: v for k, v in metadata.items() if v is not None}
                for k, v in metadata.items():
                    lines.append(f"*{k}*")
                    lines.append(f"")
                    lines.append(v)

        if len(self.data) > 0:
            import polars as pl

            lines.append("")
            try:
                content = str(pl.DataFrame(self._df_repr()))
            except:
                lines.append("#### Failed to render table")
                lines.append(
                    "An exception occured while rendering the query result in a table, but you can "
                    + "still access it in the `data` attribute of the response. Exception stacktrace:"
                )
                lines.append("```")
                lines.append(traceback.format_exc().strip())
                lines.append("```")
            else:
                lines.append("## Features")
                lines.append("```")
                split = content.split("\n")
                main = "\n".join(itertools.chain(split[1:3], split[5:]))
                lines.append(main)
                lines.append("```")

        return "\n".join(lines)

    def get_feature(self, feature: Any) -> Optional[FeatureResult]:
        # Typing `feature` as Any, as the Features will be typed as the underlying datatypes, not as Feature
        return self._values.get(str(feature))

    def get_feature_value(self, feature: Any) -> Optional[Any]:
        # Typing `feature` as Any, as the Features will be typed as the underlying datatypes, not as Feature
        v = self.get_feature(feature)
        return v and v.value

    def to_dict(self, prefix: bool = True) -> Dict[str, Any]:
        if prefix:
            return {f.field: f.value for f in self.data}
        return {f.field.split(".", maxsplit=2)[-1]: f.value for f in self.data}


class ChalkAPIClientImpl(ChalkClient):
    __name__ = "ChalkClient"
    __qualname__ = "chalk.client.ChalkClient"

    latest_client: Optional[ChalkAPIClientImpl] = None
    default_job_timeout: Optional[timedelta] = None

    def __repr__(self):
        branch_text = ""
        if self._config.branch is not None:
            branch_text = f", branch='{self._config.branch}'"
        return f"chalk.client.ChalkClient<{self._config.name}{branch_text}>"

    def __new__(cls, *args: Any, **kwargs: Any) -> ChalkClient:
        return object.__new__(ChalkAPIClientImpl)

    def __init__(  # pyright: ignore[reportMissingSuperCall]
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        environment: Optional[EnvironmentId] = None,
        api_server: Optional[str] = None,
        query_server: Optional[str] = None,
        branch: Optional[BranchId] = None,
        preview_deployment_id: Optional[DeploymentId] = None,
        _skip_cache: bool = False,
        session: Optional[requests.Session] = None,
        additional_headers: Optional[Mapping[str, str]] = None,
        default_job_timeout: float | timedelta | None = None,
        local: bool = False,
    ):
        if CHALK_IMPORT_FLAG.get() is True:
            raise RuntimeError(
                "Attempting to instantiate a Chalk client while importing source modules is forbidden. "
                + "Please exclude this file from import using your `.chalkignore` file "
                + "(see https://docs.chalk.ai/cli/apply), or wrap this query in a function that is not called upon import."
            )

        self.default_status_report_timeout = timedelta(minutes=10)

        if default_job_timeout is not None and not isinstance(default_job_timeout, timedelta):
            default_job_timeout = timedelta(seconds=default_job_timeout)
        self.default_job_timeout = default_job_timeout

        self.session = session or requests.Session()

        if session is None:
            retries = Retry(connect=3, read=3)
            self.session.mount("https://", HTTPAdapter(max_retries=retries))
            self.session.mount("http://", HTTPAdapter(max_retries=retries))

        token = load_token(
            client_id=client_id,
            client_secret=client_secret,
            active_environment=environment,
            api_server=api_server,
            skip_cache=_skip_cache,
        )
        if token is None:
            raise ChalkAuthException()

        if local and branch is None:
            branch = "chalk_local_" + "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

        api_server = token.apiServer or "https://api.chalk.ai"
        self._config = _ChalkClientConfig(
            name=token.name or "",
            client_id=token.clientId,
            client_secret=token.clientSecret,
            api_server=api_server,
            query_server=query_server or api_server,
            branch=branch,
            active_environment=token.activeEnvironment,
            preview_deployment_id=preview_deployment_id,
        )

        self._default_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": f"chalkpy-{chalkpy_version}",
            "X-Chalk-Client-Id": self._config.client_id,
            "X-Chalk-Features-Versioned": "true",
        }
        self._default_headers.update(additional_headers or {})

        self._exchanged_credentials = False
        self._primary_environment = None

        self.__class__.latest_client = self
        if notebook.is_notebook():
            if local:
                raise ValueError("Cannot use local mode in a notebook")

            # Register cell magics
            self._register_cell_magics()

            if branch is None:
                self.whoami()
            else:
                self._load_branches()

        if local:
            if branch is None:
                raise ValueError("Cannot use local mode without a branch")

            chalklocal = os.path.expanduser("~/.chalk/bin/chalk")
            if not os.path.exists(chalklocal):
                raise FileNotFoundError("Chalk CLI not found in ~/.chalk/bin/chalk, so cannot local apply")

            result = subprocess.run(
                [chalklocal, "apply", "--branch", branch],
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode != 0:
                raise RuntimeError(
                    f"Failed to apply branch '{branch}' using local source. Underlying error:\n {result.stderr}\n{result.stdout}"
                )

    @property
    def config(self):
        return self._config

    def _register_cell_magics(self):
        try:
            from IPython.core.magic import register_cell_magic
        except ImportError:
            _logger.warning("Failed to register cell magics, IPython not found")
            return

        from chalk.utils.notebook import register_resolver_from_cell_magic

        def resolver(line: str, cell: str | None):
            """Parses the cell as a SQL string resolver and uploads it to the branch"""
            from chalk.sql._internal.sql_file_resolver import SQLStringResult

            failures = register_resolver_from_cell_magic(
                sql_string_result=SQLStringResult(
                    path=re.sub(r"[^A-Za-z_\-0-9]+", "_", line.strip()),
                    sql_string=cell,
                    error=None,
                )
            )
            for failure in failures:
                print(f"Failed to register resolver:\n{failure.traceback}\n")

        register_cell_magic(resolver)

    def _exchange_credentials(self):
        _logger.debug("Performing a credentials exchange")
        resp = self._raw_session_request(
            method="post",
            url=urljoin(self._config.api_server, "v1/oauth/token"),
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            json=ExchangeCredentialsRequest(
                client_id=self._config.client_id,
                client_secret=self._config.client_secret,
                grant_type="client_credentials",
            ).dict(),
            timeout=60,
        )
        resp.raise_for_status()
        response_json = resp.json()
        try:
            creds = ExchangeCredentialsResponse(**response_json)
        except ValidationError:
            raise HTTPError(response=resp)
        self._default_headers["Authorization"] = f"Bearer {creds.access_token}"
        self._primary_environment = creds.primary_environment
        self._exchanged_credentials = True

    def _get_headers(
        self,
        environment_override: Optional[str],
        preview_deployment_id: Optional[str],
        branch: Optional[Union[BranchId, ellipsis]],
    ) -> dict[str, str]:
        x_chalk_env_id = environment_override or self._config.active_environment or self._primary_environment
        headers = dict(self._default_headers)  # shallow copy
        if x_chalk_env_id is not None:
            headers["X-Chalk-Env-Id"] = x_chalk_env_id
        if preview_deployment_id is not None:
            headers["X-Chalk-Preview-Deployment"] = preview_deployment_id

        if branch is ...:
            pass
        elif branch is not None and branch is not ...:
            headers["X-Chalk-Branch-Id"] = branch
        elif self._config.branch is not None:
            headers["X-Chalk-Branch-Id"] = self._config.branch

        return headers

    @staticmethod
    def _raise_if_200_with_errors(response: BaseModel):
        errors = getattr(response, "errors", None)
        if errors and isinstance(errors, list) and all(isinstance(e, ChalkError) for e in errors):
            errors = cast(List[ChalkError], errors)
            raise ChalkBaseException(errors=errors)

    @staticmethod
    def _raise_if_200_with_non_resolver_errors(response: BaseModel):
        errors = getattr(response, "errors", None)
        if errors and isinstance(errors, list) and all(isinstance(e, ChalkError) for e in errors):
            if any(not e.is_resolver_runtime_error() for e in errors):
                errors = cast(List[ChalkError], errors)
                raise ChalkBaseException(errors=errors)
            else:
                # Do nothing: we want to maintain the dataset with the resolver errors, but we should inform the user!
                message = """!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
WARNING: One or more resolvers failed to run. This
is very likely not a problem with Chalk, but rather
your resolvers. You can debug your resolvers through
use of the 'resolver_replay' functionality:
https://docs.chalk.ai/docs/debugging-queries#resolver-replay
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
                if notebook.is_notebook():
                    print(message)
                else:
                    _logger.info(message)

    @staticmethod
    def _raise_if_http_error(response: requests.Response, environment_override_warning: bool = False):
        if response.status_code < 400:
            return

        if response.status_code == 403 and environment_override_warning:
            raise ChalkBaseException(
                errors=None, detail="403: Cannot override environment when `client_id` and `client_secret` are set."
            )

        def _standardized_raise():
            try:
                standardized_exception = _ChalkHTTPException.parse_obj(response.json())
            except Exception:
                pass
            else:
                raise ChalkBaseException(
                    errors=standardized_exception.errors,
                    trace_id=standardized_exception.trace,
                    detail=standardized_exception.detail,
                )

        def _fallback_raise():
            trace_id = None
            if hasattr(response, "headers"):
                trace_id = response.headers.get(CHALK_TRACE_ID_KEY)

            detail = None
            try:
                response_json = response.json()
                if isinstance(response_json, Mapping):
                    detail = response_json.get("detail")
            except RequestsJSONDecodeError:
                pass

            status_code = response.status_code
            known_error_code = None
            if status_code == 401:
                known_error_code = ErrorCode.UNAUTHENTICATED
            elif status_code == 403:
                known_error_code = ErrorCode.UNAUTHORIZED

            message = (
                f"{status_code} {detail}"
                if detail
                else f"Unexpected Chalk server error while calling {response.url} with status code {status_code}"
            )
            chalk_error = ChalkError(
                code=known_error_code or ErrorCode.INTERNAL_SERVER_ERROR,
                message=message,
            )
            raise ChalkBaseException(errors=[chalk_error], trace_id=trace_id)

        _standardized_raise()
        _fallback_raise()

    def _raw_session_request(
        self,
        method: str,
        headers: Mapping[str, str],
        url: str,
        json: Mapping[str, Any] | None,
        data: str | bytes | None = None,
        timeout: float | None = None,
    ) -> requests.Response:
        try:
            return self.session.request(method=method, headers=headers, url=url, json=json, data=data, timeout=timeout)
        except ConnectionError:
            return self.session.request(method=method, headers=headers, url=url, json=json, data=data, timeout=timeout)
        except urllib3.exceptions.ConnectionError:
            return self.session.request(method=method, headers=headers, url=url, json=json, data=data, timeout=timeout)

    @overload
    def _request(
        self,
        method: str,
        uri: str,
        response: None,
        json: Optional[BaseModel],
        environment_override: Optional[str],
        preview_deployment_id: Optional[str],
        branch: Optional[Union[BranchId, ellipsis]],
        data: Optional[bytes] = None,
        api_server_override: Optional[str] = None,
        metadata_request: bool = True,
        extra_headers: Optional[dict[str, str]] = None,
        timeout: Optional[float] = None,
        route_branch_through_api_server: bool = False,
    ) -> requests.Response:
        ...

    @overload
    def _request(
        self,
        method: str,
        uri: str,
        response: Type[T],
        json: Optional[BaseModel],
        environment_override: Optional[str],
        preview_deployment_id: Optional[str],
        branch: Optional[Union[BranchId, ellipsis]],
        data: Optional[bytes] = None,
        api_server_override: Optional[str] = None,
        metadata_request: bool = True,
        extra_headers: Optional[dict[str, str]] = None,
        timeout: Optional[float] = None,
        route_branch_through_api_server: bool = False,
    ) -> T:
        ...

    def _request(
        self,
        method: str,
        uri: str,
        response: Optional[Type[T]],
        json: Optional[BaseModel],
        environment_override: Optional[str],
        preview_deployment_id: Optional[str],
        branch: Optional[Union[BranchId, ellipsis]],
        data: Optional[bytes] = None,
        api_server_override: Optional[str] = None,
        metadata_request: bool = True,
        extra_headers: Optional[dict[str, str]] = None,
        timeout: Optional[float] = None,
        route_branch_through_api_server: bool = False,
    ) -> T | requests.Response:
        if extra_headers is None:
            extra_headers = {}

        environment_override_warning = False
        is_service_account = self._config.client_id.startswith("token-")
        if (
            is_service_account
            and environment_override is not None
            and self._config.active_environment is not None
            and environment_override != self._config.active_environment
        ):
            environment_override_warning = True

        # Track whether we already exchanged credentials for this request
        exchanged_credentials = False
        if not self._exchanged_credentials:
            exchanged_credentials = True
            try:
                self._exchange_credentials()
            except HTTPError as e:
                self._raise_if_http_error(
                    response=e.response, environment_override_warning=environment_override_warning
                )
        headers = self._get_headers(
            environment_override=environment_override,
            preview_deployment_id=preview_deployment_id,
            branch=branch,
        )
        headers.update(extra_headers)
        default_api_server = self._config.api_server if metadata_request else self._config.query_server
        url = urljoin(api_server_override or default_api_server, uri)
        json_body = json and json.dict()

        if route_branch_through_api_server and "X-Chalk-Branch-Id" in headers:
            del headers["X-Chalk-Branch-Id"]

        if headers.get("X-Chalk-Branch-Id") and headers.get("X-Chalk-Env-Id"):
            status_url = urljoin(self._config.api_server, "/v1/branches/start")
            status_headers = dict(self._default_headers)
            status_headers["X-Chalk-Env-Id"] = headers["X-Chalk-Env-Id"]
            r = self.session.request(method="POST", headers=status_headers, url=status_url)

            # Only loop if the branch server needs to be started
            if r.json().get("status") == "error":
                print(
                    "The branch server is offline. Starting the server is expected to take 2 minutes but could take longer.\n"
                )
                for _ in tqdm(range(30)):
                    try:
                        r = self.session.request(method="POST", headers=status_headers, url=status_url)
                        if r.json().get("status") == "ok":
                            break
                        time.sleep(4)
                    except requests.exceptions.ConnectionError:
                        pass
                print()

                if r.json().get("status") != "ok":
                    print("The branch server is still offline. Polling for another 3 minutes...\n")
                    for _ in range(60):
                        try:
                            r = self.session.request(method="POST", headers=status_headers, url=status_url)
                            if r.json().get("status") == "ok":
                                break
                            time.sleep(3)
                        except requests.exceptions.ConnectionError:
                            pass

                if r.json().get("status") != "ok":
                    raise ChalkCustomException("The branch server did not start. Retry your query.")

                print("The branch server is online.\n")

        r = self.session.request(method=method, headers=headers, url=url, json=json_body, data=data)
        if r.status_code in (401, 403) and not exchanged_credentials:
            # It is possible that credentials expired, or that we changed permissions since we last
            # got a token. Exchange them and try again
            self._exchange_credentials()
            r = self._raw_session_request(
                method=method, headers=headers, url=url, json=json_body, data=data, timeout=timeout or 60.0
            )

        self._raise_if_http_error(response=r, environment_override_warning=environment_override_warning)
        if response is None:
            return r
        return response(**r.json())

    def _load_branches(self):
        try:
            branch = self._config.branch
            result = self._request(
                method="GET",
                uri="/v1/branches",
                response=_BranchMetadataResponse,
                json=None,
                environment_override=None,
                preview_deployment_id=None,
                branch=branch,
                api_server_override=self._get_local_server_override(None),
            )

        except ChalkBaseException as e:
            # If we can't get branches, we can't do anything else
            self._raise_bad_creds_error(errors=e.errors)
        our_branch = next((b for b in result.branches if b.name == branch), None)
        if our_branch is None:
            project_config = load_project_config()
            if project_config:
                project_path = Path(project_config.local_path).parent
            else:
                project_path = "<Your Chalk project directory>"
            branch_names = list(reversed(sorted(result.branches, key=lambda b: str(b.latest_deployment_time))))
            limit = 10
            available_branches = "\n".join(f"  - {b.name}" for b in branch_names[:limit])
            if len(branch_names) > limit:
                available_text = f"The {limit} most recently used branches are:"
            else:
                available_text = "Available branches are:"
            raise ChalkCustomException(
                f"""Your client is set up to use a branch '{branch}' that does not exist. {available_text}

{available_branches}

To deploy new features and resolvers in a Jupyter notebook, you must first create a branch from the Chalk CLI.

>>> cd "{project_path}" && chalk apply --branch "{branch}"

Then, you can run this cell again and see your new work! For more docs on applying changes to branches, see:

https://docs.chalk.ai/cli/apply
"""
            )

    def _raise_bad_creds_error(self, errors: Optional[List[ChalkError]] = None) -> NoReturn:
        exc = ChalkCustomException(
            f"""We weren't able to authenticate you with the Chalk API. Authentication was attempted with the following credentials:

    Client ID:     {self._config.client_id}
    Client Secret: {'*' * len(self._config.client_secret)}
    Branch:        {self._config.branch or ''}
    Environment:   {self._config.active_environment or ''}
    API Server:    {self._config.api_server}
    chalkpy:       v{chalkpy_version}

If these credentials look incorrect to you, try running

>>> chalk login

from the command line from '{os.getcwd()}'. If you are still having trouble, please contact Chalk support.""",
            errors=errors,
        )
        raise exc

    def whoami(self) -> WhoAmIResponse:
        try:
            return self._request(
                method="GET",
                uri="/v1/who-am-i",
                response=WhoAmIResponse,
                json=None,
                environment_override=None,
                preview_deployment_id=None,
                metadata_request=True,
                branch=None,
            )
        except ChalkBaseException as e:
            self._raise_bad_creds_error(errors=e.errors)

    # TODO can we go ahead and expose this model to clients? Seems useful
    def _get_branch_info(self) -> _BranchMetadataResponse:
        result = self._request(
            method="GET",
            uri="/v1/branches",
            response=_BranchMetadataResponse,
            json=None,
            environment_override=None,
            preview_deployment_id=None,
            branch=...,
            api_server_override=self._get_local_server_override(None),
        )
        return result

    def get_branches(self) -> List[str]:
        branches = self._get_branch_info().branches
        return sorted([b.name for b in branches])

    def get_branch(self) -> Optional[str]:
        return self._config.branch

    def set_branch(self, branch_name: Optional[str]):
        if branch_name is not None:
            branches = self._get_branch_info().branches
            if not any(x.name == branch_name for x in branches):
                raise ValueError(
                    (
                        f"A branch with the name '{branch_name}' does not exist in this environment. Run ChalkClient.create_branch(branch_name) to create a new branch. "
                        f"To see a list of available branches, use ChalkClient.get_branches()."
                    )
                )
        self._config.branch = branch_name

        message = f"Branch set to '{branch_name}'"
        if not notebook.is_notebook():
            _logger.info(message)
        else:
            print(message)

    def upload_features(
        self,
        input: Mapping[FeatureReference, Any],
        branch: Optional[Union[BranchId, ellipsis]] = ...,
        environment: Optional[EnvironmentId] = None,
        preview_deployment_id: Optional[str] = None,
        correlation_id: Optional[str] = None,
        query_name: Optional[str] = None,
        meta: Optional[Mapping[str, str]] = None,
    ) -> List[ChalkError]:
        encoded_inputs, _ = recursive_encode_inputs(input)

        # Convert to a bulk style request
        for k, v in encoded_inputs.items():
            encoded_inputs[k] = [v]

        request = UploadFeaturesRequest(
            input=cast(Mapping[str, List[Any]], encoded_inputs),
            preview_deployment_id=preview_deployment_id,
            correlation_id=correlation_id,
            query_name=query_name,
            meta=meta,
        )

        extra_headers = {}
        if query_name is not None:
            extra_headers["X-Chalk-Query-Name"] = query_name

        resp = self._request(
            method="POST",
            uri="/v1/upload_features",
            json=request,
            environment_override=environment,
            preview_deployment_id=preview_deployment_id,
            branch=branch,
            response=UploadFeaturesResponse,
            extra_headers=extra_headers,
            api_server_override=self._get_local_server_override(branch),
        )
        return resp.errors

    def multi_upload_features(
        self,
        input: Union[
            List[Mapping[Union[str, Feature, Any], Any]],
            Mapping[Union[str, Feature, Any], List[Any]],
            pd.DataFrame,
            pl.DataFrame,
            DataFrame,
        ],
        branch: Union[BranchId, ellipsis, None] = ...,
        environment: Optional[EnvironmentId] = None,
        preview_deployment_id: Optional[str] = None,
        correlation_id: Optional[str] = None,
        meta: Optional[Mapping[str, str]] = None,
    ) -> Optional[List[ChalkError]]:
        table_compression = "uncompressed"
        try:
            tables = to_multi_upload_inputs(input)
        except ChalkBaseException as e:
            return e.errors
        except Exception as e:
            return [
                ChalkError(
                    code=ErrorCode.INVALID_QUERY,
                    message="Client failed to convert inputs to a multi-upload request",
                    exception=ChalkException(
                        kind=type(e).__name__,
                        message=str(e),
                        stacktrace=traceback.format_exc(),
                    ),
                )
            ]

        import pyarrow.feather

        if branch is ...:
            branch = self._config.branch

        errors = []
        for table in tables:
            features: List[str] = [field.name for field in table.schema]
            table_buffer = BytesIO()
            pyarrow.feather.write_feather(table, dest=table_buffer, compression=table_compression)
            table_buffer.seek(0)
            request = MultiUploadFeaturesRequest(
                features=features, table_compression=table_compression, table_bytes=table_buffer.getvalue()
            )
            resp = self._request(
                method="POST",
                uri="/v1/upload_features/multi",
                data=request.serialize(),
                json=None,
                response=MultiUploadFeaturesResponse,
                environment_override=environment,
                preview_deployment_id=preview_deployment_id,
                branch=branch,
                metadata_request=True,
            )
            errors.extend(resp.errors)

        return errors

    def query(
        self,
        input: Union[Mapping[FeatureReference, Any], Any],
        output: Sequence[FeatureReference] = (),
        now: Optional[datetime] = None,
        staleness: Optional[Mapping[FeatureReference, str]] = None,
        environment: Optional[EnvironmentId] = None,
        tags: Optional[List[str]] = None,
        preview_deployment_id: Optional[str] = None,
        branch: Union[BranchId, None, ellipsis] = ...,
        correlation_id: Optional[str] = None,
        query_name: Optional[str] = None,
        query_name_version: Optional[str] = None,
        include_meta: bool = False,
        meta: Optional[Mapping[str, str]] = None,
        explain: Union[bool, Literal["only"]] = False,
        store_plan_stages: bool = False,
        encoding_options: Optional[FeatureEncodingOptions] = None,
        required_resolver_tags: Optional[List[str]] = None,
        planner_options: Optional[Mapping[str, Union[str, int, bool]]] = None,
        request_timeout: Optional[float] = None,
        value_metrics_tag_by_features: Sequence[FeatureReference] = (),
    ) -> OnlineQueryResponseImpl:
        encoded_inputs, all_warnings = recursive_encode_inputs(input)
        outputs, encoding_warnings = encode_outputs(output)
        all_warnings += encoding_warnings
        encoded_value_metrics_tag_by_features, encoding_warnings = encode_outputs(value_metrics_tag_by_features)
        all_warnings += encoding_warnings

        if branch is ...:
            branch = self._config.branch

        if preview_deployment_id is None:
            preview_deployment_id = self._config.preview_deployment_id

        now_str = None
        if now is not None:
            if now.tzinfo is None:
                now = now.astimezone(tz=timezone.utc)
            now_str = now.isoformat()

        staleness_encoded = {}
        if staleness is not None:
            for k, v in staleness.items():
                if is_feature_set_class(k):
                    for f in k.features:
                        staleness_encoded[f.root_fqn] = v
                else:
                    staleness_encoded[ensure_feature(k).root_fqn] = v

        request = OnlineQueryRequest(
            inputs=encoded_inputs,
            outputs=outputs,
            now=now_str,
            staleness=staleness_encoded,
            context=OnlineQueryContext(
                environment=environment,
                tags=tags,
                required_resolver_tags=required_resolver_tags,
            ),
            deployment_id=preview_deployment_id,
            branch_id=branch,
            correlation_id=correlation_id,
            query_name=query_name,
            query_name_version=query_name_version,
            meta=meta,
            explain=explain,
            include_meta=bool(include_meta or explain),
            store_plan_stages=store_plan_stages,
            encoding_options=encoding_options or FeatureEncodingOptions(),
            planner_options=planner_options,
            value_metrics_tag_by_features=tuple(encoded_value_metrics_tag_by_features),
        )

        extra_headers = {}
        if query_name is not None:
            extra_headers["X-Chalk-Query-Name"] = query_name

        resp = self._request(
            method="POST",
            uri="/v1/query/online",
            json=request,
            response=OnlineQueryResponse,
            environment_override=environment,
            preview_deployment_id=preview_deployment_id,
            branch=branch,
            metadata_request=False,
            extra_headers=extra_headers,
            api_server_override=self._get_local_server_override(None),
            timeout=request_timeout,
        )
        return OnlineQueryResponseImpl(data=resp.data, errors=resp.errors or [], warnings=all_warnings, meta=resp.meta)

    def multi_query(
        self,
        queries: list[OnlineQuery],
        environment: Optional[EnvironmentId] = None,
        preview_deployment_id: Optional[str] = None,
        branch: Optional[Union[BranchId, ellipsis]] = ...,
        correlation_id: Optional[str] = None,
        query_name: Optional[str] = None,
        query_name_version: Optional[str] = None,
        meta: Optional[Mapping[str, str]] = None,
        use_feather: Optional[bool] = True,  # deprecated
        compression: Optional[str] = "uncompressed",
    ) -> BulkOnlineQueryResponse:
        if branch is ...:
            branch = self._config.branch
        extra_headers = {}
        if query_name is not None:
            extra_headers["X-Chalk-Query-Name"] = query_name
        buffer = BytesIO()
        buffer.write(MULTI_QUERY_MAGIC_STR)
        all_warnings: List[str] = []
        if preview_deployment_id is None:
            preview_deployment_id = self._config.preview_deployment_id
        for query in queries:
            tags = query.tags
            encoded_inputs = {str(k): v for k, v in query.input.items()}
            outputs, encoding_warnings = encode_outputs(query.output)
            all_warnings += encoding_warnings
            encoded_value_metrics_tag_by_features, encoding_warnings = encode_outputs(
                query.value_metrics_tag_by_features
            )
            all_warnings += encoding_warnings
            request = OnlineQueryManyRequest(
                inputs=cast(Mapping[str, List[Any]], encoded_inputs),
                outputs=outputs,
                staleness=(
                    {}
                    if query.staleness is None
                    else {ensure_feature(k).root_fqn: v for k, v in query.staleness.items()}
                ),
                context=OnlineQueryContext(
                    environment=environment,
                    tags=None if tags is None else list(tags),
                ),
                deployment_id=preview_deployment_id,
                branch_id=branch,
                correlation_id=correlation_id,
                query_name=query_name,
                query_name_version=query_name_version,
                meta=meta,
                value_metrics_tag_by_features=tuple(encoded_value_metrics_tag_by_features),
            )

            write_query_to_buffer(buffer, request, compression=compression)

        buffer.seek(0)
        resp = self._request(
            method="POST",
            uri="/v1/query/feather",
            data=buffer.getvalue(),
            json=None,
            response=None,
            environment_override=environment,
            preview_deployment_id=preview_deployment_id,
            branch=branch,
            metadata_request=False,
            extra_headers=extra_headers,
        )

        if resp.headers.get("Content-Type") == "application/octet-stream":
            all_responses = OnlineQueryResponseFeather.deserialize(resp.content)

            bulk_results = []
            for query_name, serialized_single_result in all_responses.query_results_bytes.items():
                single_feather_result = OnlineQueryResultFeather.deserialize(serialized_single_result)
                scalars_df = None
                groups_dfs = None
                query_meta = QueryMeta(**json.loads(single_feather_result.meta)) if single_feather_result.meta else None
                errors = (
                    [ChalkError(**json.loads(error_json_str)) for error_json_str in single_feather_result.errors]
                    if single_feather_result.errors
                    else None
                )
                if single_feather_result.has_data:
                    scalars_pa = pyarrow.feather.read_table(BytesIO(single_feather_result.scalar_data))
                    scalars_pl = pa_table_to_pl_df(scalars_pa)
                    scalars_df = scalars_pl

                    groups_dfs = {}
                    for feature_name, feature_results_bytes in single_feather_result.groups_data.items():
                        feature_pa = pyarrow.feather.read_table(BytesIO(feature_results_bytes))
                        feature_pl = pa_table_to_pl_df(feature_pa)
                        groups_dfs[feature_name] = feature_pl

                bulk_result = BulkOnlineQueryResult(
                    scalars_df=scalars_df, groups_dfs=groups_dfs, errors=errors, meta=query_meta
                )
                bulk_results.append(bulk_result)
            return BulkOnlineQueryResponse(results=bulk_results)
        else:
            raise ChalkBaseException(
                errors=None, detail="Unexpected response from server -- failed to receive Feather encoded data."
            )

    def query_bulk(
        self,
        input: Union[Mapping[FeatureReference, Sequence[Any]], Any],
        output: Sequence[FeatureReference],
        now: Optional[Sequence[datetime]] = None,
        staleness: Optional[Mapping[FeatureReference, str]] = None,
        context: Optional[OnlineQueryContext] = None,  # Deprecated.
        environment: Optional[EnvironmentId] = None,
        store_plan_stages: bool = False,
        tags: Optional[List[str]] = None,
        required_resolver_tags: Optional[List[str]] = None,
        preview_deployment_id: Optional[str] = None,
        branch: Optional[Union[BranchId, ellipsis]] = ...,
        correlation_id: Optional[str] = None,
        query_name: Optional[str] = None,
        query_name_version: Optional[str] = None,
        meta: Optional[Mapping[str, str]] = None,
        value_metrics_tag_by_features: Sequence[FeatureReference] = (),
    ) -> BulkOnlineQueryResponse:
        if branch is ...:
            branch = self._config.branch

        if preview_deployment_id is None:
            preview_deployment_id = self._config.preview_deployment_id

        extra_headers = {}
        if query_name is not None:
            extra_headers["X-Chalk-Query-Name"] = query_name

        now_str = None
        if now is not None:
            now_str = []
            for ts in now:
                if ts.tzinfo is None:
                    ts = ts.astimezone(tz=timezone.utc)
                now_str.append(ts.isoformat())

        staleness_encoded = {}
        if staleness is not None:
            for k, v in staleness.items():
                if is_feature_set_class(k):
                    for f in k.features:
                        staleness_encoded[f.root_fqn] = v
                else:
                    staleness_encoded[ensure_feature(k).root_fqn] = v

        environment = environment or (context and context.environment)
        tags = tags or (context and context.tags)
        # TODO: We're doing a lame encoding here b/c recursive_encode will treat our lists
        #       as json to serialize.
        # encoded_inputs, encoding_warnings = recursive_encode(input)
        encoded_inputs = {str(k): v for k, v in input.items()}
        outputs, _ = encode_outputs(output)
        encoded_value_metrics_tag_by_features, _ = encode_outputs(value_metrics_tag_by_features)
        request = OnlineQueryManyRequest(
            inputs=cast(Mapping[str, List[Any]], encoded_inputs),
            outputs=outputs,
            now=now_str,
            staleness=staleness_encoded,
            context=OnlineQueryContext(
                environment=environment,
                tags=tags,
                required_resolver_tags=required_resolver_tags,
            ),
            deployment_id=preview_deployment_id,
            branch_id=branch,
            correlation_id=correlation_id,
            query_name=query_name,
            query_name_version=query_name_version,
            meta=meta,
            store_plan_stages=store_plan_stages,
            # explain=explain,
            value_metrics_tag_by_features=tuple(encoded_value_metrics_tag_by_features),
        )

        buffer = BytesIO()

        buffer.write(MULTI_QUERY_MAGIC_STR)
        write_query_to_buffer(buffer, request, compression="uncompressed")

        buffer.seek(0)

        resp = self._request(
            method="POST",
            uri="/v1/query/feather",
            data=buffer.getvalue(),
            json=None,
            response=None,
            environment_override=environment,
            preview_deployment_id=preview_deployment_id,
            branch=branch,
            metadata_request=False,
            extra_headers=extra_headers,
        )

        import polars as pl
        import pyarrow.feather

        assert (
            resp.headers.get("Content-Type") == "application/octet-stream"
        ), "The response wasn't in the expected byte format!"
        all_responses = OnlineQueryResponseFeather.deserialize(resp.content)

        bulk_results = []
        for query_name, serialized_single_result in all_responses.query_results_bytes.items():
            single_feather_result = OnlineQueryResultFeather.deserialize(serialized_single_result)
            scalars_df = None
            groups_dfs = None
            query_meta = QueryMeta(**json.loads(single_feather_result.meta)) if single_feather_result.meta else None
            errors = (
                [ChalkError(**json.loads(error_json_str)) for error_json_str in single_feather_result.errors]
                if single_feather_result.errors
                else None
            )
            if single_feather_result.has_data:
                scalars_pa = pyarrow.feather.read_table(BytesIO(single_feather_result.scalar_data))
                scalars_pl = pa_table_to_pl_df(scalars_pa)
                assert isinstance(scalars_pl, pl.DataFrame)
                scalars_df = scalars_pl

                groups_dfs = {}
                for feature_name, feature_results_bytes in single_feather_result.groups_data.items():
                    feature_pa = pyarrow.feather.read_table(BytesIO(feature_results_bytes))
                    feature_pl = pa_table_to_pl_df(feature_pa)
                    groups_dfs[feature_name] = feature_pl

            bulk_result = BulkOnlineQueryResult(
                scalars_df=scalars_df, groups_dfs=groups_dfs, errors=errors, meta=query_meta
            )
            bulk_results.append(bulk_result)
        return BulkOnlineQueryResponse(results=bulk_results)

    def offline_query(
        self,
        input: Union[QueryInput, Tuple[QueryInput, ...], List[QueryInput], None] = None,
        input_times: Union[Sequence[datetime], datetime, Sequence[Sequence[datetime]], None] = None,
        output: Sequence[FeatureReference] = (),
        required_output: Sequence[FeatureReference] = (),
        environment: Optional[EnvironmentId] = None,
        dataset_name: Optional[str] = None,
        branch: Optional[Union[BranchId, ellipsis]] = ...,
        # distinguished from user explicitly specifying branch=None
        correlation_id: str | None = None,
        max_samples: Optional[int] = None,
        wait: bool = False,
        show_progress: bool = True,
        timeout: float | timedelta | ellipsis | None = ...,
        recompute_features: Union[bool, List[FeatureReference]] = False,
        sample_features: Optional[List[FeatureReference]] = None,
        lower_bound: datetime | str | None = None,
        upper_bound: datetime | str | None = None,
        store_plan_stages: bool = False,
        explain: Union[bool, Literal["only"]] = False,
        tags: Optional[List[str]] = None,
        required_resolver_tags: Optional[List[str]] = None,
        planner_options: Optional[Mapping[str, Union[str, int, bool]]] = None,
        spine_sql_query: str | None = None,
        resources: ResourceRequests | None = None,
        include_meta: Optional[
            bool
        ] = None,  # unused, undocumented. provided to make switching online_query -> offline_query easier.
        run_asynchronously: bool = False,
        use_multiple_computers: bool = False,
        upload_input_as_table: bool = False,
        # if set, will upload the input in parquet to cloud storage instead of sending it in the request
    ) -> DatasetImpl:
        run_asynchronously = use_multiple_computers or run_asynchronously

        lower_bound = _convert_datetime_param("lower_bound", lower_bound)
        upper_bound = _convert_datetime_param("upper_bound", upper_bound)

        if branch is ...:
            branch = self._config.branch

        try:
            import polars as pl
        except ImportError:
            raise missing_dependency_exception("chalkpy[runtime]")
        del pl  # unused

        if len(output) == 0 and len(required_output) == 0:
            raise ValueError("Either 'output' or 'required_output' must be specified.")
        optional_output_root_fqns = [str(f) for f in output]
        required_output_root_fqns = [str(f) for f in required_output]

        context = OfflineQueryContext(environment=environment)

        if input is None:
            multi_query_input = None
        elif isinstance(input, (list, tuple)):
            input_times_tuple: Sequence[QueryInputTime] = (
                [None] * len(input)
                if input_times is None
                else [input_times for _ in input]
                if isinstance(input_times, datetime)
                else input_times
            )
            run_asynchronously = True
            multi_query_input = tuple(_to_offline_query_input(qi, times) for qi, times in zip(input, input_times_tuple))
        else:
            multi_query_input = (_to_offline_query_input(input, cast(None, input_times)),)

        if multi_query_input is None:
            query_input = None
        elif upload_input_as_table:
            with ThreadPoolExecutor(thread_name_prefix="offline_query_upload_input") as upload_input_executor:
                query_input = self._upload_offline_query_input(
                    multi_query_input, context=context, branch=branch, executor=upload_input_executor
                )
        elif run_asynchronously:
            query_input = multi_query_input
        else:
            assert len(multi_query_input) == 1, "We should default to running asynchronously if inputs is partitioned"
            query_input = multi_query_input[0]

        response = self._create_dataset_job(
            optional_output=optional_output_root_fqns,
            required_output=required_output_root_fqns,
            query_input=query_input,
            spine_sql_query=spine_sql_query,
            dataset_name=dataset_name,
            branch=branch,
            correlation_id=correlation_id,
            context=context,
            max_samples=max_samples,
            recompute_features=recompute_features,
            sample_features=sample_features,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
            store_plan_stages=store_plan_stages,
            tags=tags,
            required_resolver_tags=required_resolver_tags,
            planner_options=planner_options,
            run_asynchronously=run_asynchronously,
            explain=explain,
            resources=resources,
        )

        initialized_dataset = dataset_from_response(response, self)

        revision = initialized_dataset.revisions[-1]
        assert isinstance(revision, DatasetRevisionImpl)
        # Storing timeout for when we call dataset revision methods that
        # require polling
        revision.timeout = timeout

        if not wait:
            return initialized_dataset

        revision.wait_for_completion(show_progress=show_progress, timeout=timeout, caller_method="offline_query")
        initialized_dataset.is_finished = True
        return initialized_dataset

    def get_operation_feature_statistics(self, operation_id: uuid.UUID) -> FeatureStatisticsResponse:
        """
        Fetches statistics for an operation's outputs.
        """
        return self._request(
            "GET",
            f"/v1/operations/{operation_id}/feature_statistics",
            FeatureStatisticsResponse,
            json=None,
            environment_override=None,
            preview_deployment_id=None,
            branch=None,
            api_server_override=self._get_local_server_override(None),
        )

    def ingest_dataset(
        self,
        request: IngestDatasetRequest,
        context: OfflineQueryContext,
    ) -> DatasetImpl:
        response = self._request(
            method="POST",
            uri="/v4/ingest_dataset",
            json=request,
            response=DatasetResponse,
            environment_override=context.environment,
            preview_deployment_id=None,
            branch=request.branch,
            metadata_request=False,
            route_branch_through_api_server=True,
        )
        ingestion_dataset = dataset_from_response(response, self)
        return ingestion_dataset.wait(show_progress=False, caller_name="ingest_dataset")

    def sample(
        self,
        output: Sequence[FeatureReference] = (),
        required_output: Sequence[FeatureReference] = (),
        output_id: bool = False,
        output_ts: Union[bool, str] = False,
        max_samples: Optional[int] = None,
        dataset: Optional[str] = None,
        branch: Optional[BranchId] = None,
        environment: Optional[EnvironmentId] = None,
        tags: Optional[List[str]] = None,
        timeout: float | timedelta | ellipsis | None = ...,
    ) -> pd.DataFrame:
        try:
            import polars as pl
        except ImportError:
            raise missing_dependency_exception("chalkpy[runtime]")
        context = OfflineQueryContext(environment=environment)
        optional_output_root_fqns = [str(f) for f in output]
        required_output_root_fqns = [str(f) for f in required_output]

        if len(output) == 0 and len(required_output) == 0:
            raise ValueError("Either 'output' or 'required_output' must be specified.")

        response = self._create_and_await_offline_query_job(
            query_input=None,
            optional_output=optional_output_root_fqns,
            required_output=required_output_root_fqns,
            max_samples=max_samples,
            context=context,
            output_id=output_id,
            output_ts=output_ts,
            dataset_name=dataset,
            branch=branch,
            preview_deployment_id=None,
            lazy=False,
            timeout=timeout,
            tags=tags,
        )
        if isinstance(response, pl.LazyFrame):
            response = response.collect()

        return response.to_pandas()

    @overload
    def get_dataset(
        self,
        dataset_name: str,
        environment: EnvironmentId | None = None,
    ) -> Dataset:
        ...

    @overload
    def get_dataset(
        self,
        *,
        revision_id: str | uuid.UUID,
        environment: EnvironmentId | None = None,
    ) -> Dataset:
        ...

    @overload
    def get_dataset(
        self,
        *,
        job_id: str | uuid.UUID,
        environment: EnvironmentId | None = None,
    ) -> Dataset:
        ...

    @overload
    def get_dataset(
        self,
        *,
        dataset_id: str | uuid.UUID,
        environment: EnvironmentId | None = None,
    ) -> Dataset:
        ...

    def get_dataset(
        self,
        dataset_name: Optional[str] = None,
        environment: Optional[EnvironmentId] = None,
        *,
        dataset_id: str | uuid.UUID | None = None,
        revision_id: str | uuid.UUID | None = None,
        job_id: str | uuid.UUID | None = None,
    ) -> Dataset:
        if sum([dataset_name is not None, dataset_id is not None, revision_id is not None, job_id is not None]) != 1:
            raise ValueError(
                "'ChalkClient.get_dataset' must be called with exactly one of 'dataset_name', 'dataset_id' or 'job_id'"
            )

        if revision_id is not None:
            response: DatasetResponse = self._get_dataset_from_job_id(
                job_id=revision_id,
                environment=environment,
                branch=None,
            )
        elif job_id is not None:
            response: DatasetResponse = self._get_dataset_from_job_id(
                job_id=job_id,
                environment=environment,
                branch=None,
            )
        elif dataset_id is not None:
            response: DatasetResponse = self._get_dataset_from_name_or_id(
                dataset_name_or_id=str(dataset_id), environment=environment, branch=None
            )
        elif dataset_name is not None:
            response: DatasetResponse = self._get_dataset_from_name_or_id(
                dataset_name_or_id=dataset_name, environment=environment, branch=None
            )
        else:
            raise ValueError(
                "'ChalkClient.get_dataset' must be called with exactly one of 'dataset_name', 'dataset_id' or 'job_id'"
            )
        if response.errors:
            raise ChalkCustomException(
                message=f"Failed to download dataset `{dataset_name}`",
                errors=response.errors,
            )
        return dataset_from_response(response, self)

    def delete_features(
        self,
        namespace: str,
        features: Optional[List[str]],
        tags: Optional[List[str]],
        primary_keys: List[str],
        environment: Optional[EnvironmentId] = None,
    ) -> FeatureObservationDeletionResponse:
        if self._config.branch is not None:
            raise NotImplementedError(
                f"Feature deletion is not currently supported for branch deployments. Client is currently connected to the branch '{self._config.branch}'."
            )
        _logger.debug(
            (
                f"Performing deletion in environment {environment if environment else 'default'} and namespace "
                f"{namespace} with targets that match the following criteria: features={features}, tags={tags}, "
                f"and primary_keys={primary_keys}"
            )
        )

        return self._request(
            method="DELETE",
            uri="/v1/features/rows",
            json=FeatureObservationDeletionRequest(
                namespace=namespace,
                features=features,
                tags=tags,
                primary_keys=primary_keys,
            ),
            response=FeatureObservationDeletionResponse,
            environment_override=environment,
            preview_deployment_id=None,
            branch=None,
        )

    def drop_features(
        self,
        namespace: str,
        features: List[str],
        environment: Optional[EnvironmentId] = None,
    ) -> FeatureDropResponse:
        if self._config.branch is not None:
            raise NotImplementedError(
                f"Feature dropping is not currently supported for branch deployments. Client is currently connected to the branch '{self._config.branch}'."
            )
        _logger.debug(
            (
                f"Performing feature drop in environment {environment if environment else 'default'} and namespace "
                f"{namespace} for the following features:{features}."
            )
        )
        return self._request(
            method="DELETE",
            uri="/v1/features/columns",
            json=FeatureDropRequest(namespace=namespace, features=features),
            response=FeatureDropResponse,
            environment_override=environment,
            preview_deployment_id=None,
            branch=None,
        )

    def trigger_resolver_run(
        self,
        resolver_fqn: str,
        environment: Optional[EnvironmentId] = None,
        preview_deployment_id: Optional[str] = None,
        branch: Optional[Union[BranchId, ellipsis]] = ...,
        upper_bound: datetime | str | None = None,
        lower_bound: datetime | str | None = None,
        store_online: bool = True,
        store_offline: bool = True,
        timestamping_mode: Literal["feature_time", "online_store_write_time"] = "feature_time",
        override_target_image_tag: str | None = None,
    ) -> ResolverRunResponse:
        if branch is ...:
            branch = self._config.branch

        if branch is not None:
            raise NotImplementedError(
                (
                    f"Triggering resolver runs is not currently supported for branch deployments."
                    f"Client is currently connected to the branch '{self._config.branch}'."
                )
            )
        if preview_deployment_id is None:
            preview_deployment_id = self._config.preview_deployment_id
        _logger.debug(f"Triggering resolver {resolver_fqn} to run")

        lower_bound = _convert_datetime_param("lower_bound", lower_bound)
        upper_bound = _convert_datetime_param("upper_bound", upper_bound)

        return self._request(
            method="POST",
            uri="/v1/runs/trigger",
            json=TriggerResolverRunRequest(
                resolver_fqn=resolver_fqn,
                lower_bound=lower_bound and lower_bound.isoformat(),
                upper_bound=upper_bound and upper_bound.isoformat(),
                timestamping_mode=timestamping_mode,
                persistence_settings=PersistenceSettings(
                    persist_online_storage=store_online, persist_offline_storage=store_offline
                ),
                override_target_image_tag=override_target_image_tag,
            ),
            response=ResolverRunResponse,
            environment_override=environment,
            preview_deployment_id=preview_deployment_id,
            branch=branch,
        )

    def get_run_status(
        self,
        run_id: str,
        environment: Optional[EnvironmentId] = None,
        preview_deployment_id: Optional[str] = None,
        branch: Optional[Union[BranchId, ellipsis]] = ...,
    ) -> ResolverRunResponse:
        if branch is ...:
            branch = self._config.branch
        if branch is not None:
            raise NotImplementedError(
                (
                    f"Triggering resolver runs is not currently supported for branch deployments."
                    f"Client is currently connected to the branch '{self._config.branch}'."
                )
            )
        response = self._request(
            method="GET",
            uri=f"/v1/runs/{run_id}",
            response=ResolverRunResponse,
            json=None,
            environment_override=environment,
            preview_deployment_id=preview_deployment_id,
            branch=branch,
        )

        return response

    def _create_and_await_offline_query_job(
        self,
        optional_output: List[str],
        required_output: List[str],
        query_input: Optional[OfflineQueryInput],
        max_samples: Optional[int],
        dataset_name: Optional[str],
        branch: Optional[BranchId],
        context: OfflineQueryContext,
        output_id: bool,
        output_ts: Union[bool, str],
        preview_deployment_id: Optional[str],
        lazy: bool,
        tags: Optional[List[str]],
        timeout: float | timedelta | ellipsis | None,
    ) -> Union[pl.DataFrame, pl.LazyFrame]:
        req = CreateOfflineQueryJobRequest(
            output=optional_output,
            required_output=required_output,
            destination_format="PARQUET",
            input=query_input,
            max_samples=max_samples,
            dataset_name=dataset_name,
            branch=branch,
            recompute_features=True,
            tags=tags,
        )
        response = self._create_offline_query_job(
            request=req,
            context=context,
            preview_deployment_id=preview_deployment_id,
            branch=branch,
        )
        self._raise_if_200_with_errors(response=response)
        if timeout is None:
            deadline = None
        else:
            if timeout is ...:
                timeout = self.default_status_report_timeout
            if not isinstance(timeout, timedelta):
                timeout = timedelta(seconds=timeout)
            deadline = datetime.now() + timeout
        while deadline is None or datetime.now() < deadline:
            status = self.get_job_status_v4(
                request=DatasetJobStatusRequest(
                    job_id=str(response.job_id),
                    ignore_errors=False,
                    query_inputs=False,
                ),
                environment=context and context.environment,
                branch=branch,
            )
            if status.is_finished:
                break
            time.sleep(0.5)
        else:
            raise TimeoutError(
                "Offline query job did not complete before timeout. The job may have failed or may still be running."
            )
        if status.errors:
            raise ChalkBaseException(errors=status.errors)
        return load_dataset(
            uris=status.urls,
            output_features=[*optional_output, *required_output],
            version=DatasetVersion(status.version),
            output_id=output_id,
            output_ts=output_ts,
            columns=status.columns,
            lazy=lazy,
        )

    def load_dataset(
        self,
        job_id: uuid.UUID,
        outputs: Sequence[str] | None,
        output_id: bool,
        output_ts: bool | str,
        context: Optional[OfflineQueryContext],
        branch: Optional[BranchId],
        ignore_errors: bool,
        query_inputs: bool,
    ) -> pl.LazyFrame:
        status = self.get_job_status_v4(
            request=DatasetJobStatusRequest(
                job_id=str(job_id),
                ignore_errors=ignore_errors,
                query_inputs=query_inputs,
            ),
            environment=context and context.environment,
            branch=branch,
        )
        return load_dataset(
            uris=status.urls,
            output_features=outputs,
            version=DatasetVersion(status.version),
            columns=status.columns,
            output_id=output_id,
            output_ts=output_ts,
            lazy=True,
        ).lazy()

    def recompute_dataset(
        self,
        dataset_name: Optional[str],
        revision_id: uuid.UUID,
        features: List[Union[str, Any]] | None,
        branch: BranchId | None,
        environment: Optional[EnvironmentId],
        correlation_id: str | None = None,
        wait: bool = False,
        show_progress: bool = True,
        store_plan_stages: bool = False,
        explain: Union[bool, Literal["only"]] = False,
        tags: Optional[List[str]] = None,
        required_resolver_tags: Optional[List[str]] = None,
        planner_options: Optional[Mapping[str, Union[str, int, bool]]] = None,
        use_multiple_computers: bool = False,
        timeout: float | timedelta | ellipsis | None = ...,
    ) -> DatasetImpl:
        outputs = [str(f) for f in features] if features else []
        req = CreateOfflineQueryJobRequest(
            output=outputs,
            required_output=[],
            destination_format="PARQUET",
            input=None,
            dataset_name=dataset_name,
            branch=branch,
            recompute_features=outputs if outputs != [] else True,
            store_plan_stages=store_plan_stages,
            correlation_id=correlation_id,
            explain=explain,
            tags=tags,
            required_resolver_tags=required_resolver_tags,
            use_multiple_computers=use_multiple_computers,
            planner_options=planner_options,
            recompute_request_revision_id=str(revision_id),
        )
        response = self._create_dataset_request(
            request=req,
            context=OfflineQueryContext(environment=environment),
            preview_deployment_id=None,
            branch=branch,
            route_branch_through_api_server=use_multiple_computers,
        )
        self._raise_if_200_with_non_resolver_errors(response=response)

        initialized_dataset = dataset_from_response(response, self)

        revision = initialized_dataset.revisions[-1]
        assert isinstance(revision, DatasetRevisionImpl)
        # Storing timeout for when we call dataset revision methods that
        # require polling
        revision.timeout = timeout

        if not wait:
            return initialized_dataset

        revision.wait_for_completion(show_progress=show_progress, timeout=timeout, caller_method="recompute")
        initialized_dataset.is_finished = True
        return initialized_dataset

    def _upload_offline_query_input(
        self,
        offline_query_inputs: Sequence[OfflineQueryInput],
        context: OfflineQueryContext,
        branch: Optional[BranchId],
        executor: ThreadPoolExecutor,
    ) -> UploadedParquetShardedOfflineQueryInput:
        urls = self._get_offline_query_input_upload_url(
            num_partitions=len(offline_query_inputs),
            context=context,
            branch=branch,
        )
        if len(offline_query_inputs) != len(urls.urls):
            raise ValueError(
                f"The number of signed upload URLs {len(urls.urls)}, input data {len(offline_query_inputs)} must be equal. "
            )
        tables = _offline_query_inputs_to_parquet(offline_query_inputs)
        futs: List[Future[None]] = []
        for annotated_url, table in zip(urls.urls, tables):
            futs.append(
                executor.submit(
                    _upload_table_parquet,
                    table,
                    annotated_url.signed_url,
                )
            )
        for fut in futs:
            fut.result()
        return UploadedParquetShardedOfflineQueryInput(
            filenames=tuple(annotated_url.filename for annotated_url in urls.urls),
            version=OfflineQueryGivensVersion.SINGLE_TS_COL_NAME_WITH_URI_PREFIX,
        )

    def _get_offline_query_input_upload_url(
        self,
        num_partitions: int,
        context: OfflineQueryContext,
        branch: Optional[BranchId],
    ) -> OfflineQueryParquetUploadURLResponse:
        response = self._request(
            method="GET",
            uri=f"/v1/offline_query_parquet_upload_url/{num_partitions}",
            json=None,
            response=OfflineQueryParquetUploadURLResponse,
            environment_override=context.environment,
            preview_deployment_id=None,
            branch=branch,
            api_server_override=self._get_local_server_override(branch),
            metadata_request=False,
            route_branch_through_api_server=False,
        )
        self._raise_if_200_with_errors(response=response)
        return response

    def _create_dataset_job(
        self,
        optional_output: List[str],
        required_output: List[str],
        query_input: Union[
            Tuple[OfflineQueryInput, ...], Optional[OfflineQueryInput], UploadedParquetShardedOfflineQueryInput
        ],
        max_samples: Optional[int],
        dataset_name: Optional[str],
        branch: Optional[BranchId],
        context: OfflineQueryContext,
        correlation_id: Optional[str] = None,
        recompute_features: Union[bool, List[FeatureReference]] = False,
        sample_features: Optional[List[FeatureReference]] = None,
        lower_bound: Optional[datetime] = None,
        upper_bound: Optional[datetime] = None,
        store_plan_stages: bool = False,
        explain: Union[bool, Literal["only"]] = False,
        tags: Optional[List[str]] = None,
        required_resolver_tags: Optional[List[str]] = None,
        planner_options: Optional[Mapping[str, Union[str, int, bool]]] = None,
        run_asynchronously: bool = False,
        spine_sql_query: str | None = None,
        resources: ResourceRequests | None = None,
    ) -> DatasetResponse:
        if not (
            isinstance(recompute_features, list)
            or isinstance(recompute_features, bool)  # pyright: ignore[reportUnnecessaryIsInstance]
        ):
            raise ValueError("The value for 'recompute_features' must be either a bool for a list of features.")
        if sample_features is not None and not isinstance(
            sample_features, list
        ):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise ValueError("The value for 'sample_features' must be a list of features.")
        if isinstance(recompute_features, list):
            recompute_features = [
                unwrap_feature(f).fqn if isinstance(f, FeatureWrapper) else f for f in recompute_features
            ]
        if isinstance(sample_features, list):
            sample_features = [unwrap_feature(f).fqn if isinstance(f, FeatureWrapper) else f for f in sample_features]
        if isinstance(recompute_features, list) and isinstance(sample_features, list):
            intersection = set(recompute_features) & set(sample_features)
            if len(intersection) > 0:
                raise ValueError(
                    "Features in 'recompute_features' and 'sample_features' arguments must not overlap. "
                    + f"Intersection as specified is {sorted(list(intersection))}"
                )
        if lower_bound and lower_bound.tzinfo is None:
            lower_bound = lower_bound.astimezone()
        if upper_bound and upper_bound.tzinfo is None:
            upper_bound = upper_bound.astimezone()

        req = CreateOfflineQueryJobRequest(
            output=optional_output,
            required_output=required_output,
            destination_format="PARQUET",
            input=query_input,
            max_samples=max_samples,
            dataset_name=dataset_name,
            branch=branch,
            recompute_features=recompute_features,
            sample_features=sample_features,
            observed_at_lower_bound=lower_bound and lower_bound.isoformat(),
            observed_at_upper_bound=upper_bound and upper_bound.isoformat(),
            store_plan_stages=store_plan_stages,
            correlation_id=correlation_id,
            explain=explain,
            tags=tags,
            required_resolver_tags=required_resolver_tags,
            planner_options=planner_options,
            use_multiple_computers=run_asynchronously,
            spine_sql_query=spine_sql_query,
            resources=resources,
        )
        response = self._create_dataset_request(
            request=req,
            context=context,
            preview_deployment_id=None,
            branch=branch,
            route_branch_through_api_server=run_asynchronously,
        )
        self._raise_if_200_with_non_resolver_errors(response=response)
        return response

    def compute_resolver_output(
        self,
        input: Union[Mapping[Union[str, Feature], Any], pl.DataFrame, pd.DataFrame, DataFrame],
        input_times: List[datetime],
        resolver: str,
        context: Optional[OfflineQueryContext] = None,
        preview_deployment_id: Optional[str] = None,
        branch: Optional[BranchId] = None,
        timeout: timedelta | float | ellipsis | None = ...,
    ) -> pl.DataFrame:
        try:
            import polars as pl
        except ImportError:
            raise missing_dependency_exception("chalkpy[runtime]")
        if context is None:
            context = OfflineQueryContext()
        query_input = _to_offline_query_input(input, input_times)
        request = ComputeResolverOutputRequest(input=query_input, resolver_fqn=resolver)
        response = self._request(
            method="POST",
            uri="/v1/compute_resolver_output",
            json=request,
            response=ComputeResolverOutputResponse,
            environment_override=context.environment,
            preview_deployment_id=preview_deployment_id,
            branch=branch,
        )
        self._raise_if_200_with_errors(response=response)

        if timeout is None:
            deadline = None
        else:
            if timeout is ...:
                timeout = self.default_status_report_timeout
            if not isinstance(timeout, timedelta):
                timeout = timedelta(seconds=timeout)
            deadline = datetime.now() + timeout
        while deadline is None or datetime.now() < deadline:
            status = self._get_compute_job_status(
                job_id=response.job_id,
                context=context,
                preview_deployment_id=preview_deployment_id,
                branch=branch,
            )
            if status.is_finished:
                break
            time.sleep(0.5)
        else:
            raise TimeoutError(
                f"Computing outputs for resolver {resolver} did not finish before the timeout. The job may still be running or may have failed."
            )

        df = load_dataset(
            uris=status.urls,
            version=status.version,
            executor=None,
            columns=status.columns,
        )
        if isinstance(df, pl.LazyFrame):
            df = df.collect()
        return df

    def create_branch(
        self,
        branch_name: str,
        create_only: bool = False,
        switch: bool = True,
        source_deployment_id: Optional[str] = None,
        environment: Optional[EnvironmentId] = None,
    ) -> BranchDeployResponse:
        available_branches = self.get_branches()
        if branch_name in available_branches and create_only:
            raise RuntimeError(
                (
                    f"The branch `{branch_name}` already exists."
                    f" To connect your client to an existing branch, specify the 'branch' parameter when "
                    f"creating a ChalkClient. Available branches are: {available_branches}"
                )
            )

        request = BranchDeployRequest(
            branch_name=branch_name,
            create_only=create_only,
            source_deployment_id=source_deployment_id,
        )
        try:
            resp = self._request(
                method="POST",
                uri=f"/v1/branches/{branch_name}/source",
                response=BranchDeployResponse,
                json=request,
                branch=...,
                environment_override=environment,
                preview_deployment_id=None,
            )
        except ChalkBaseException as e:
            raise ChalkCustomException.from_base(e, f"Failed to deploy branch `{branch_name}`.")

        if notebook.is_notebook():
            self._display_branch_creation_response(resp)

            if switch:
                self.set_branch(branch_name)
            else:
                self._display_button_to_change_branch(branch_name)
        return resp

    def _display_branch_creation_response(self, resp: BranchDeployResponse):
        from IPython.display import display_markdown

        if resp.new_branch_created:
            prefix = "Created new "
        else:
            prefix = "Deployed "
        text = f"{prefix} branch `{resp.branch_name}` with source from deployment `{resp.source_deployment_id}`."
        display_markdown(text, raw=True)

    def _display_button_to_change_branch(self, branch_name: str):
        if not notebook.is_notebook():
            return
        try:
            from IPython.core.display_functions import display
            from ipywidgets import widgets

            layout = widgets.Layout(width="auto")
            button0 = widgets.Button(
                description=f"Set current branch to '{branch_name}'",
                tooltip=f'Equivalent to client.set_branch("{branch_name}")',
                layout=layout,
            )
            output0 = widgets.Output()
            display(button0, output0)

            def on_button_clicked0(_):
                with output0:
                    old_branch = self._config.branch
                    self._config.branch = branch_name
                    old_branch_text = ""
                    if old_branch is not None:
                        old_branch_text = f" from `{old_branch}`"
                    from IPython.display import display_markdown

                    display_markdown(f"Set branch for Chalk client{old_branch_text} to `{branch_name}`.", raw=True)

            button0.on_click(on_button_clicked0)
        except Exception:
            pass

    def _get_compute_job_status(
        self,
        job_id: str,
        context: OfflineQueryContext,
        preview_deployment_id: Optional[str],
        branch: Optional[BranchId] = None,
    ) -> GetOfflineQueryJobResponse:
        return self._request(
            method="GET",
            uri=f"/v1/compute_resolver_output/{job_id}",
            response=GetOfflineQueryJobResponse,
            json=None,
            environment_override=context.environment,
            preview_deployment_id=preview_deployment_id,
            branch=branch,
        )

    def _create_dataset_request(
        self,
        request: CreateOfflineQueryJobRequest,
        context: OfflineQueryContext,
        preview_deployment_id: str | None,
        branch: BranchId | None = None,
        route_branch_through_api_server: bool = False,
    ) -> DatasetResponse:
        response = self._request(
            method="POST",
            uri="/v4/offline_query",
            json=request,
            response=DatasetResponse,
            environment_override=context.environment,
            preview_deployment_id=preview_deployment_id,
            branch=branch,
            api_server_override=None if route_branch_through_api_server else self._get_local_server_override(branch),
            metadata_request=False,
            route_branch_through_api_server=route_branch_through_api_server,
        )
        return response

    def _create_offline_query_job(
        self,
        request: CreateOfflineQueryJobRequest,
        context: OfflineQueryContext,
        preview_deployment_id: Optional[str],
        branch: Optional[BranchId] = None,
    ):
        response = self._request(
            method="POST",
            uri="/v2/offline_query",
            json=request,
            response=CreateOfflineQueryJobResponse,
            environment_override=context.environment,
            preview_deployment_id=preview_deployment_id,
            branch=branch,
        )
        return response

    def get_job_status_v4(
        self, request: DatasetJobStatusRequest, environment: Optional[EnvironmentId], branch: Optional[BranchId]
    ) -> GetOfflineQueryJobResponse:
        return self._request(
            method="POST",
            uri="/v4/offline_query/status",
            response=GetOfflineQueryJobResponse,
            environment_override=environment,
            json=request,
            preview_deployment_id=None,
            branch=branch,
            api_server_override=self._get_local_server_override(branch),
        )

    def get_revision_summary(
        self,
        revision_id: str,
        environment: Optional[EnvironmentId],
    ) -> DatasetRevisionSummaryResponse:
        return self._request(
            method="GET",
            uri=f"/v4/offline_query/{revision_id}/summary",
            response=DatasetRevisionSummaryResponse,
            environment_override=environment,
            json=None,
            preview_deployment_id=None,
            branch=None,
        )

    def get_revision_preview(
        self,
        revision_id: str,
        environment: Optional[EnvironmentId],
    ) -> DatasetRevisionPreviewResponse:
        return self._request(
            method="GET",
            uri=f"/v4/offline_query/{revision_id}/preview",
            response=DatasetRevisionPreviewResponse,
            environment_override=environment,
            json=None,
            preview_deployment_id=None,
            branch=None,
        )

    def _get_query_inputs(
        self, job_id: uuid.UUID, environment: Optional[EnvironmentId], branch: Optional[BranchId]
    ) -> GetOfflineQueryJobResponse:
        return self._request(
            method="GET",
            uri=f"/v2/offline_query_inputs/{job_id}",
            response=GetOfflineQueryJobResponse,
            environment_override=environment,
            json=None,
            preview_deployment_id=None,
            branch=branch,
            api_server_override=self._get_local_server_override(branch),
        )

    def _get_dataset_from_name_or_id(
        self,
        *,
        dataset_name_or_id: str,
        environment: Optional[EnvironmentId],
        branch: Optional[BranchId],
    ) -> DatasetResponse:
        return self._request(
            method="GET",
            uri=f"/v3/offline_query/{dataset_name_or_id}",
            response=DatasetResponse,
            environment_override=environment,
            json=None,
            preview_deployment_id=None,
            branch=branch,
        )

    def _get_dataset_from_job_id(
        self,
        *,
        job_id: str | uuid.UUID,
        environment: Optional[EnvironmentId],
        branch: Optional[BranchId],
        api_server_override: str | None = None,
    ) -> DatasetResponse:
        return self._request(
            method="GET",
            uri=f"/v4/offline_query/{job_id}",
            response=DatasetResponse,
            environment_override=environment,
            json=None,
            preview_deployment_id=None,
            branch=branch,
            api_server_override=api_server_override,
        )

    def get_anonymous_dataset(
        self, revision_id: str, environment: Optional[EnvironmentId], branch: Optional[BranchId]
    ) -> DatasetImpl:
        try:
            response = self._get_dataset_from_job_id(
                job_id=revision_id,
                environment=environment,
                branch=branch,
                api_server_override=self._get_local_server_override(branch),
            )
        except ChalkBaseException as e:
            raise ChalkCustomException.from_base(
                e,
                message=f"Failed to get dataset for revision id '{revision_id}'.",
            )

        return dataset_from_response(response, self)

    def get_batch_report(
        self, operation_id: uuid.UUID, environment_id: EnvironmentId, computer_id: int
    ) -> Optional[BatchReport]:
        if computer_id == 0:
            uri = f"/v4/offline_query/{operation_id}/status"
        else:
            uri = f"/v4/offline_query/{operation_id}/status/{computer_id}"
        try:
            response = self._request(
                method="GET",
                uri=uri,
                response=BatchReportResponse,
                json=None,
                environment_override=environment_id,
                preview_deployment_id=None,
                branch=...,
            )
        except Exception:
            return None

        return response.report

    def get_resolver_replay(
        self,
        environment_id: EnvironmentId,
        revision_id: uuid.UUID,
        resolver_fqn: str,
        branch: Optional[BranchId],
        timeout: float | timedelta | ellipsis | None,
    ) -> ResolverReplayResponse:
        if timeout is None:
            deadline = None
        else:
            if timeout is ...:
                timeout = self.default_status_report_timeout
            if not isinstance(timeout, timedelta):
                timeout = timedelta(seconds=timeout)
            deadline = datetime.now() + timeout
        while deadline is None or datetime.now() < deadline:
            status = self.get_job_status_v4(
                request=DatasetJobStatusRequest(
                    job_id=str(revision_id),
                    ignore_errors=False,
                    query_inputs=False,
                ),
                environment=environment_id,
                branch=branch,
            )
            if status.is_finished:
                break
            time.sleep(0.5)
        else:
            raise TimeoutError("Resolver replay timed out. The job may still be running or may have failed.")
        return self._request(
            method="GET",
            uri=f"/v4/resolver_replay/{revision_id}/{resolver_fqn}",
            response=ResolverReplayResponse,
            json=None,
            preview_deployment_id=None,
            environment_override=environment_id,
            branch=branch,
        )

    def send_updated_entity(
        self, environment: Optional[EnvironmentId], pickled_entity: bytes
    ) -> UpdateGraphEntityResponse:
        resp = self._request(
            method="POST",
            uri="/v1/update_graph_entity",
            response=UpdateGraphEntityResponse,
            json=None,
            data=pickled_entity,
            environment_override=environment,
            preview_deployment_id=None,
            branch=None,
            api_server_override=self._get_local_server_override(None),
        )
        if resp.errors:
            raise ChalkBaseException(errors=resp.errors)
        return resp

    _send_updated_entity = send_updated_entity  # backcompat

    def await_operation_completion(
        self,
        operation_id: uuid.UUID,
        environment_id: EnvironmentId,
        show_progress: bool,
        caller_method: Optional[str],
        num_computers: int,
        timeout: float | timedelta | ellipsis | None,
        raise_on_dataset_failure: bool,
    ):
        if timeout is ...:
            timeout = self.default_status_report_timeout

        for computer_id in range(num_computers):
            ProgressService(
                operation_id=operation_id,
                client=self,
                caller_method=caller_method,
                environment_id=environment_id,
                num_computers=num_computers,
                # Only showing progress for the first computer, because it would conflict
                # if multiple computers are showing results concurrently
                show_progress=show_progress and computer_id == 0,
            ).await_operation(
                computer_id=computer_id,
                must_fail_on_resolver_error=raise_on_dataset_failure,
                timeout=timeout,
            )

    def _get_local_server_override(self, body_branch: Union[BranchId, ellipsis, None]) -> Optional[str]:
        branched = (body_branch is not None and body_branch is not ...) or self._config.branch is not None
        server = self._config.api_server
        is_local = server.startswith("http://localhost") or server.startswith("http://127.0.0.1")

        server_override = None
        if branched and is_local:
            server_override = "http://localhost:1337"

        return server_override

    def _get_upsert_graph_gql_from_branch(
        self,
        branch: Union[BranchId, ellipsis, None] = ...,
        environment: Optional[EnvironmentId] = None,
    ) -> dict:
        if branch is ...:
            branch = self._config.branch
        if branch is None:
            raise RuntimeError("No branch specified or set in client. This method only works for branch deployments.")
        available_branches = self.get_branches()
        if branch not in available_branches:
            raise RuntimeError(
                (
                    f"The branch `{branch}` does not exist. "
                    f"Available branches are: {available_branches}. "
                    f"To create a branch, use `ChalkClient.create_branch(...)`"
                )
            )
        result = self._request(
            method="GET",
            uri=f"/v1/branch/{branch}/graph_gql",
            environment_override=environment,
            branch=branch,
            api_server_override=self._get_local_server_override(branch),
            response=None,  # get the JSON
            preview_deployment_id=None,
            json=None,
        )
        return result.json()

    def reset_branch(self, branch: BranchIdParam = ..., environment: Optional[EnvironmentId] = None):
        if branch is ...:
            branch = self._config.branch
        if branch is None:
            raise RuntimeError("No branch specified or set in client. This method only works for branch deployments.")
        available_branches = self.get_branches()
        if branch not in available_branches:
            raise RuntimeError(
                (
                    f"The branch `{branch}` does not exist. "
                    f"Available branches are: {available_branches}. "
                    f"To create a branch, use `ChalkClient.create_branch(...)`"
                )
            )
        self._request(
            method="POST",
            uri=f"/v1/branch/{branch}/reset",
            environment_override=environment,
            branch=branch,
            api_server_override=self._get_local_server_override(branch),
            response=None,
            preview_deployment_id=None,
            json=None,
        )

    def branch_state(
        self,
        branch: Union[BranchId, ellipsis, None] = ...,
        environment: Optional[EnvironmentId] = None,
    ) -> BranchGraphSummary:
        if branch is ...:
            branch = self._config.branch
        if branch is None:
            raise RuntimeError("No branch specified or set in client. This method only works for branch deployments.")
        available_branches = self.get_branches()
        if branch not in available_branches:
            raise RuntimeError(
                (
                    f"The branch `{branch}` does not exist. "
                    f"Available branches are: {available_branches}. "
                    f"To create a branch, use `ChalkClient.create_branch(...)`"
                )
            )
        result = self._request(
            method="GET",
            uri=f"/v1/branch/{branch}/graph_state",
            environment_override=environment,
            branch=branch,
            api_server_override=self._get_local_server_override(branch),
            response=None,  # get the JSON
            preview_deployment_id=None,
            json=None,
        )
        return BranchGraphSummary.from_dict(result.json())  # type: ignore

    def test_streaming_resolver(
        self,
        resolver: Union[str, Resolver],
        num_messages: Optional[int] = None,
        message_filepath: Optional[str] = None,
        message_keys: Optional[List[str]] = None,
        message_bodies: Optional[List[Union[str, bytes]]] = None,
        message_timestamps: Optional[List[Union[str, datetime]]] = None,
        branch: Union[BranchId, ellipsis, None] = ...,
        environment: Optional[EnvironmentId] = None,
    ) -> StreamResolverTestResponse:
        resolver_fqn = resolver.fqn if isinstance(resolver, Resolver) else resolver
        if branch is ...:
            branch = self._config.branch

        if num_messages is None and message_filepath is None and (message_keys is None or message_bodies is None):
            raise ValueError(
                (
                    "One of 'num_messages', 'test_message_filepath' or ('test_message_keys' and 'test_message_bodies')"
                    " must be provided."
                )
            )
        payloads = (
            self._validate_test_stream_resolver_inputs(
                message_filepath=message_filepath,
                message_keys=message_keys,
                message_bodies=message_bodies,
                message_timestamps=message_timestamps,
            )
            if message_keys is not None or message_filepath is not None
            else None
        )
        request = StreamResolverTestRequest(
            resolver_fqn=resolver_fqn, num_messages=num_messages, test_messages=payloads
        )
        result = self._request(
            method="POST",
            uri=f"/v1/test_stream_resolver/",
            environment_override=environment,
            json=request,
            branch=branch,
            api_server_override=self._get_local_server_override(branch),
            response=StreamResolverTestResponse,
            preview_deployment_id=None,
        )
        return result

    def _validate_test_stream_resolver_inputs(
        self,
        message_filepath: Optional[str] = None,
        message_keys: Optional[List[str]] = None,
        message_bodies: Optional[List[Union[str, bytes]]] = None,
        message_timestamps: Optional[List[Union[str, datetime]]] = None,
    ) -> List[StreamResolverTestMessagePayload]:
        if message_filepath and (message_keys or message_bodies):
            raise ValueError("Only one of 'message_filepath' or ('message_keys' and 'message_bodies') can be provided.")
        if sum([message_keys is None, message_bodies is None]) == 1:
            raise ValueError("Both of 'message_keys' and 'message_bodies' must be provided")
        if message_filepath:
            message_keys = []
            message_bodies = []
            message_timestamps = []
            with open(message_filepath) as file:
                for i, line in enumerate(file):
                    try:
                        json_message = json.loads(line.rstrip())
                        if "message_key" not in json_message:
                            raise ValueError(f"Key 'message_key' missing from line {i + 1}")
                        if "message_body" not in json_message:
                            raise ValueError(f"Key 'message_body' missing from line {i + 1}")
                        message_keys.append(json_message["message_key"])
                        message_bodies.append(json.dumps(json_message["message_body"]))
                        if "message_timestamp" in json_message:
                            timestamp_string = json_message["message_timestamp"]
                            message_timestamps.append(timestamp_string)
                    except Exception as e:
                        raise ValueError(f"Could not parse line {line} from file {message_filepath}: error {e}")

        assert message_keys is not None
        assert message_bodies is not None
        if len(message_keys) != len(message_bodies) or len(message_keys) == 0:
            raise ValueError(
                (
                    f"The length of 'message_keys' and the length of 'message_bodies' must be equal and nonzero. "
                    f"{len(message_keys)} != {len(message_bodies)}"
                )
            )
        if message_timestamps and len(message_keys) != len(message_timestamps):
            raise ValueError(
                (
                    f"The length of 'message_keys' and the length of 'message_timestamps' must be equal and nonzero. "
                    f"{len(message_keys)} != {len(message_bodies)}"
                )
            )
        if message_timestamps:
            timestamp_datetimes = []
            for timestamp in message_timestamps:
                try:
                    if isinstance(timestamp, str):
                        timestamp = parser.parse(timestamp)
                    if timestamp.tzinfo is None:
                        raise ValueError(f"timestamp {timestamp} must be timezone aware")
                    timestamp_datetimes.append(timestamp)
                except Exception as e:
                    raise ValueError(f"Could not parse timestamp {timestamp}, {e}")
        else:
            timestamp_datetimes = None
        bodies_are_bytes = True if isinstance(message_bodies[0], bytes) else False
        if bodies_are_bytes:
            message_bodies = [base64.b64encode(cast(bytes, message)).decode("utf-8") for message in message_bodies]
        payloads: List[StreamResolverTestMessagePayload] = [
            StreamResolverTestMessagePayload(
                key=message_keys[i],
                message_str=cast(str, message_bodies[i]) if not bodies_are_bytes else None,
                message_bytes=cast(str, message_bodies[i]) if bodies_are_bytes else None,
                timestamp=timestamp_datetimes[i] if timestamp_datetimes is not None else None,
            )
            for i in range(len(message_keys))
        ]
        return payloads

    @override
    def plan_query(
        self,
        input: Sequence[FeatureReference],
        output: Sequence[FeatureReference],
        staleness: Optional[Mapping[FeatureReference, str]] = None,
        environment: Optional[EnvironmentId] = None,
        tags: Optional[List[str]] = None,
        preview_deployment_id: Optional[str] = None,
        branch: Union[BranchId, None, ellipsis] = ...,
        query_name: Optional[str] = None,
        query_name_version: Optional[str] = None,
        meta: Optional[Mapping[str, str]] = None,
    ) -> PlanQueryResponse:
        all_warnings: List[str] = []
        encoded_inputs, encoding_warnings = encode_outputs(input)
        all_warnings += encoding_warnings
        outputs, encoding_warnings = encode_outputs(output)
        all_warnings += encoding_warnings

        if branch is ...:
            branch = self._config.branch

        if preview_deployment_id is None:
            preview_deployment_id = self._config.preview_deployment_id

        staleness_encoded = {}
        if staleness is not None:
            for k, v in staleness.items():
                if is_feature_set_class(k):
                    for f in k.features:
                        staleness_encoded[f.root_fqn] = v
                else:
                    staleness_encoded[ensure_feature(k).root_fqn] = v

        request = PlanQueryRequest(
            inputs=encoded_inputs,
            outputs=outputs,
            staleness=staleness_encoded,
            context=OnlineQueryContext(
                environment=environment,
                tags=tags,
            ),
            deployment_id=preview_deployment_id,
            branch_id=branch,
            query_name=query_name,
            query_name_version=query_name_version,
            meta=meta,
        )

        extra_headers = {}
        if query_name is not None:
            extra_headers["X-Chalk-Query-Name"] = query_name

        resp = self._request(
            method="POST",
            uri="/v1/query/plan",
            json=request,
            response=PlanQueryResponse,
            environment_override=environment,
            preview_deployment_id=preview_deployment_id,
            branch=branch,
            metadata_request=False,
            extra_headers=extra_headers,
            api_server_override=self._get_local_server_override(None),
        )
        return resp

    def set_incremental_cursor(
        self,
        *,
        resolver: str | Resolver | None = None,
        scheduled_query: str | None = None,
        max_ingested_timestamp: datetime | None = None,
        last_execution_timestamp: datetime | None = None,
    ) -> None:
        if scheduled_query is None and resolver is None:
            raise ValueError("Either scheduled_query or resolver must be provided")
        if scheduled_query is not None and resolver is not None:
            raise ValueError("Exactly one of scheduled_query or resolver must be provided")

        if scheduled_query is not None:
            url = f"/v1/incremental_progress/named_query/{scheduled_query}"
        else:
            url = f"/v1/resolvers/{str(resolver)}/incremental_progress"

        self._request(
            method="POST",
            uri=url,
            data=SetIncrementalProgressRequest(
                max_ingested_timestamp=max_ingested_timestamp.astimezone(tz=timezone.utc)
                if max_ingested_timestamp
                else None,
                last_execution_timestamp=last_execution_timestamp.astimezone(tz=timezone.utc)
                if last_execution_timestamp
                else None,
            )
            .json()
            .encode("utf-8"),
            json=None,
            response=None,
            branch=None,
            preview_deployment_id=None,
            environment_override=None,
        )

        return None

    def get_incremental_cursor(
        self, *, resolver: str | Resolver | None = None, scheduled_query: str | None = None
    ) -> GetIncrementalProgressResponse:
        if scheduled_query is None and resolver is None:
            raise ValueError("Either scheduled_query or resolver must be provided")
        if scheduled_query is not None and resolver is not None:
            raise ValueError("Exactly one of scheduled_query or resolver must be provided")

        if scheduled_query is not None:
            url = f"/v1/incremental_progress/named_query/{scheduled_query}"
        else:
            url = f"/v1/resolvers/{str(resolver)}/incremental_progress"

        return self._request(
            method="GET",
            uri=url,
            json=None,
            response=GetIncrementalProgressResponse,
            branch=None,
            preview_deployment_id=None,
            environment_override=None,
        )
