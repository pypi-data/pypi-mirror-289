from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class AggregateBackfillEstimate(_message.Message):
    __slots__ = (
        "max_buckets",
        "expected_buckets",
        "expected_bytes",
        "expected_storage_cost",
        "expected_runtime",
    )
    MAX_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_BYTES_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_STORAGE_COST_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    max_buckets: int
    expected_buckets: int
    expected_bytes: int
    expected_storage_cost: float
    expected_runtime: _duration_pb2.Duration
    def __init__(
        self,
        max_buckets: _Optional[int] = ...,
        expected_buckets: _Optional[int] = ...,
        expected_bytes: _Optional[int] = ...,
        expected_storage_cost: _Optional[float] = ...,
        expected_runtime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...,
    ) -> None: ...

class AggregateBackfillUserParams(_message.Message):
    __slots__ = (
        "features",
        "resolver",
        "timestamp_column_name",
        "lower_bound",
        "upper_bound",
        "exact",
    )
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    RESOLVER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    EXACT_FIELD_NUMBER: _ClassVar[int]
    features: _containers.RepeatedScalarFieldContainer[str]
    resolver: str
    timestamp_column_name: str
    lower_bound: _timestamp_pb2.Timestamp
    upper_bound: _timestamp_pb2.Timestamp
    exact: bool
    def __init__(
        self,
        features: _Optional[_Iterable[str]] = ...,
        resolver: _Optional[str] = ...,
        timestamp_column_name: _Optional[str] = ...,
        lower_bound: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        upper_bound: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        exact: bool = ...,
    ) -> None: ...
