"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from abc import (
    ABCMeta,
    abstractmethod,
)
from chalk._gen.chalk.server.v1.deploy_pb2 import (
    DeployBranchRequest,
    DeployBranchResponse,
    GetDeploymentRequest,
    GetDeploymentResponse,
    ListDeploymentsRequest,
    ListDeploymentsResponse,
    ScaleDeploymentRequest,
    ScaleDeploymentResponse,
    SuspendDeploymentRequest,
    SuspendDeploymentResponse,
    TagDeploymentRequest,
    TagDeploymentResponse,
)
from grpc import (
    Channel,
    Server,
    ServicerContext,
    UnaryUnaryMultiCallable,
)

class DeployServiceStub:
    def __init__(self, channel: Channel) -> None: ...
    DeployBranch: UnaryUnaryMultiCallable[
        DeployBranchRequest,
        DeployBranchResponse,
    ]
    GetDeployment: UnaryUnaryMultiCallable[
        GetDeploymentRequest,
        GetDeploymentResponse,
    ]
    ListDeployments: UnaryUnaryMultiCallable[
        ListDeploymentsRequest,
        ListDeploymentsResponse,
    ]
    SuspendDeployment: UnaryUnaryMultiCallable[
        SuspendDeploymentRequest,
        SuspendDeploymentResponse,
    ]
    ScaleDeployment: UnaryUnaryMultiCallable[
        ScaleDeploymentRequest,
        ScaleDeploymentResponse,
    ]
    TagDeployment: UnaryUnaryMultiCallable[
        TagDeploymentRequest,
        TagDeploymentResponse,
    ]

class DeployServiceServicer(metaclass=ABCMeta):
    @abstractmethod
    def DeployBranch(
        self,
        request: DeployBranchRequest,
        context: ServicerContext,
    ) -> DeployBranchResponse: ...
    @abstractmethod
    def GetDeployment(
        self,
        request: GetDeploymentRequest,
        context: ServicerContext,
    ) -> GetDeploymentResponse: ...
    @abstractmethod
    def ListDeployments(
        self,
        request: ListDeploymentsRequest,
        context: ServicerContext,
    ) -> ListDeploymentsResponse: ...
    @abstractmethod
    def SuspendDeployment(
        self,
        request: SuspendDeploymentRequest,
        context: ServicerContext,
    ) -> SuspendDeploymentResponse: ...
    @abstractmethod
    def ScaleDeployment(
        self,
        request: ScaleDeploymentRequest,
        context: ServicerContext,
    ) -> ScaleDeploymentResponse: ...
    @abstractmethod
    def TagDeployment(
        self,
        request: TagDeploymentRequest,
        context: ServicerContext,
    ) -> TagDeploymentResponse: ...

def add_DeployServiceServicer_to_server(
    servicer: DeployServiceServicer, server: Server
) -> None: ...
