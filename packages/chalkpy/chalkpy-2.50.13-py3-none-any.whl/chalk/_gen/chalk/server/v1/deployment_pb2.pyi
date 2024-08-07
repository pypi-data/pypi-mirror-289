from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class DeploymentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEPLOYMENT_STATUS_UNSPECIFIED: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_UNKNOWN: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_PENDING: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_QUEUED: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_WORKING: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_SUCCESS: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_FAILURE: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_INTERNAL_ERROR: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_TIMEOUT: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_CANCELLED: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_EXPIRED: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_BOOT_ERRORS: _ClassVar[DeploymentStatus]
    DEPLOYMENT_STATUS_AWAITING_SOURCE: _ClassVar[DeploymentStatus]

DEPLOYMENT_STATUS_UNSPECIFIED: DeploymentStatus
DEPLOYMENT_STATUS_UNKNOWN: DeploymentStatus
DEPLOYMENT_STATUS_PENDING: DeploymentStatus
DEPLOYMENT_STATUS_QUEUED: DeploymentStatus
DEPLOYMENT_STATUS_WORKING: DeploymentStatus
DEPLOYMENT_STATUS_SUCCESS: DeploymentStatus
DEPLOYMENT_STATUS_FAILURE: DeploymentStatus
DEPLOYMENT_STATUS_INTERNAL_ERROR: DeploymentStatus
DEPLOYMENT_STATUS_TIMEOUT: DeploymentStatus
DEPLOYMENT_STATUS_CANCELLED: DeploymentStatus
DEPLOYMENT_STATUS_EXPIRED: DeploymentStatus
DEPLOYMENT_STATUS_BOOT_ERRORS: DeploymentStatus
DEPLOYMENT_STATUS_AWAITING_SOURCE: DeploymentStatus

class InstanceSizing(_message.Message):
    __slots__ = ("min_instances", "max_instances")
    MIN_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    min_instances: int
    max_instances: int
    def __init__(
        self, min_instances: _Optional[int] = ..., max_instances: _Optional[int] = ...
    ) -> None: ...

class Deployment(_message.Message):
    __slots__ = ("id", "environment_id", "status", "deployment_tags")
    ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    environment_id: str
    status: DeploymentStatus
    deployment_tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        id: _Optional[str] = ...,
        environment_id: _Optional[str] = ...,
        status: _Optional[_Union[DeploymentStatus, str]] = ...,
        deployment_tags: _Optional[_Iterable[str]] = ...,
    ) -> None: ...
