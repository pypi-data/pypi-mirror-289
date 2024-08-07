"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from abc import (
    ABCMeta,
    abstractmethod,
)
from chalk._gen.chalk.server.v1.audit_pb2 import (
    GetAuditLogsRequest,
    GetAuditLogsResponse,
)
from grpc import (
    Channel,
    Server,
    ServicerContext,
    UnaryUnaryMultiCallable,
)

class AuditServiceStub:
    def __init__(self, channel: Channel) -> None: ...
    GetAuditLogs: UnaryUnaryMultiCallable[
        GetAuditLogsRequest,
        GetAuditLogsResponse,
    ]

class AuditServiceServicer(metaclass=ABCMeta):
    @abstractmethod
    def GetAuditLogs(
        self,
        request: GetAuditLogsRequest,
        context: ServicerContext,
    ) -> GetAuditLogsResponse: ...

def add_AuditServiceServicer_to_server(
    servicer: AuditServiceServicer, server: Server
) -> None: ...
