# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from chalk._gen.chalk.common.v1 import (
    query_log_pb2 as chalk_dot_common_dot_v1_dot_query__log__pb2,
)
from chalk._gen.chalk.common.v1 import (
    query_values_pb2 as chalk_dot_common_dot_v1_dot_query__values__pb2,
)


class OfflineStoreServiceStub(object):
    """This service exposes endpoints for dealing with the offline store. It should never depend on the python graph."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetQueryLogEntries = channel.unary_unary(
            "/chalk.engine.v1.OfflineStoreService/GetQueryLogEntries",
            request_serializer=chalk_dot_common_dot_v1_dot_query__log__pb2.GetQueryLogEntriesRequest.SerializeToString,
            response_deserializer=chalk_dot_common_dot_v1_dot_query__log__pb2.GetQueryLogEntriesResponse.FromString,
        )
        self.GetQueryValues = channel.unary_unary(
            "/chalk.engine.v1.OfflineStoreService/GetQueryValues",
            request_serializer=chalk_dot_common_dot_v1_dot_query__values__pb2.GetQueryValuesRequest.SerializeToString,
            response_deserializer=chalk_dot_common_dot_v1_dot_query__values__pb2.GetQueryValuesResponse.FromString,
        )


class OfflineStoreServiceServicer(object):
    """This service exposes endpoints for dealing with the offline store. It should never depend on the python graph."""

    def GetQueryLogEntries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetQueryValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_OfflineStoreServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetQueryLogEntries": grpc.unary_unary_rpc_method_handler(
            servicer.GetQueryLogEntries,
            request_deserializer=chalk_dot_common_dot_v1_dot_query__log__pb2.GetQueryLogEntriesRequest.FromString,
            response_serializer=chalk_dot_common_dot_v1_dot_query__log__pb2.GetQueryLogEntriesResponse.SerializeToString,
        ),
        "GetQueryValues": grpc.unary_unary_rpc_method_handler(
            servicer.GetQueryValues,
            request_deserializer=chalk_dot_common_dot_v1_dot_query__values__pb2.GetQueryValuesRequest.FromString,
            response_serializer=chalk_dot_common_dot_v1_dot_query__values__pb2.GetQueryValuesResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "chalk.engine.v1.OfflineStoreService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class OfflineStoreService(object):
    """This service exposes endpoints for dealing with the offline store. It should never depend on the python graph."""

    @staticmethod
    def GetQueryLogEntries(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/chalk.engine.v1.OfflineStoreService/GetQueryLogEntries",
            chalk_dot_common_dot_v1_dot_query__log__pb2.GetQueryLogEntriesRequest.SerializeToString,
            chalk_dot_common_dot_v1_dot_query__log__pb2.GetQueryLogEntriesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetQueryValues(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/chalk.engine.v1.OfflineStoreService/GetQueryValues",
            chalk_dot_common_dot_v1_dot_query__values__pb2.GetQueryValuesRequest.SerializeToString,
            chalk_dot_common_dot_v1_dot_query__values__pb2.GetQueryValuesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
