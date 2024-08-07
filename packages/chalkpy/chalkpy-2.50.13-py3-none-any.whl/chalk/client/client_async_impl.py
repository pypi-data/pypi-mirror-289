from __future__ import annotations

import asyncio
import types
import warnings
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
from functools import partial
from typing import Any, Mapping, Optional, TypeVar, Union
from uuid import UUID

import requests
import requests.adapters

from chalk.client import AsyncChalkClient
from chalk.client.client_impl import ChalkAPIClientImpl, OnlineQueryResponseImpl
from chalk.client.dataset import DatasetImpl
from chalk.client.models import BulkOnlineQueryResponse, FeatureStatisticsResponse, WhoAmIResponse
from chalk.features.tag import BranchId, DeploymentId, EnvironmentId
from chalk.utils.log_with_context import get_logger
from chalk.utils.threading import DEFAULT_IO_EXECUTOR

_logger = get_logger(__name__)

T = TypeVar("T")


class AsyncChalkClientImpl(AsyncChalkClient):
    __name__ = "AsyncChalkClient"
    __qualname__ = "chalk.client.AsyncChalkClient"

    def __repr__(self):
        return self._client.__repr__().replace("chalk.client.ChalkClient", "chalk.client.AsyncChalkClient")

    def __new__(cls, *args: Any, **kwargs: Any) -> AsyncChalkClient:
        return object.__new__(AsyncChalkClientImpl)

    def __init__(  # pyright: ignore[reportMissingSuperCall]
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        environment: Optional[EnvironmentId] = None,
        api_server: Optional[str] = None,
        query_server: Optional[str] = None,
        branch: Optional[BranchId] = None,
        preview_deployment_id: Optional[DeploymentId] = None,
        additional_headers: Optional[Mapping[str, str]] = None,
        default_job_timeout: Optional[Union[float, timedelta]] = None,
        executor: Optional[ThreadPoolExecutor] = None,
        pool_maxsize: Optional[int] = None,
    ):
        self._executor = executor or DEFAULT_IO_EXECUTOR
        session = requests.Session()
        if pool_maxsize is not None:
            adapter = requests.adapters.HTTPAdapter(pool_maxsize=pool_maxsize)
            session.mount("http://", adapter)
            session.mount("https://", adapter)
        self._client: ChalkAPIClientImpl = ChalkAPIClientImpl(
            client_id=client_id,
            client_secret=client_secret,
            environment=environment,
            api_server=api_server,
            query_server=query_server,
            branch=branch,
            preview_deployment_id=preview_deployment_id,
            session=session,
            additional_headers=additional_headers,
            default_job_timeout=default_job_timeout,
        )  # pyright: ignore[reportAttributeAccessIssue]

    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: types.TracebackType | None,
    ):
        return

    def __enter__(self):
        warnings.warn(DeprecationWarning("Use `async with`, not `with`, with the AsyncChalkClient"))
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: types.TracebackType | None,
    ):
        return

    def _current_loop(self):
        return asyncio.get_running_loop()

    async def whoami(self) -> WhoAmIResponse:
        return await self._current_loop().run_in_executor(
            self._executor,
            self._client.whoami,
        )

    async def query(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> OnlineQueryResponseImpl:
        return await self._current_loop().run_in_executor(
            self._executor,
            partial(self._client.query, *args, **kwargs),
        )

    async def multi_query(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> BulkOnlineQueryResponse:
        return await self._current_loop().run_in_executor(
            self._executor,
            partial(self._client.multi_query, *args, **kwargs),
        )

    async def query_bulk(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> BulkOnlineQueryResponse:
        return await self._current_loop().run_in_executor(
            self._executor,
            partial(self._client.query_bulk, *args, **kwargs),
        )

    async def offline_query(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> DatasetImpl:
        return await self._current_loop().run_in_executor(
            self._executor,
            partial(self._client.offline_query, *args, **kwargs),
        )

    async def get_operation_feature_statistics(self, operation_id: UUID) -> FeatureStatisticsResponse:
        return await self._current_loop().run_in_executor(
            self._executor,
            partial(self._client.get_operation_feature_statistics, operation_id),
        )
