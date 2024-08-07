# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chalk/server/v1/audit.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chalk._gen.chalk.auth.v1 import agent_pb2 as chalk_dot_auth_dot_v1_dot_agent__pb2
from chalk._gen.chalk.auth.v1 import (
    permissions_pb2 as chalk_dot_auth_dot_v1_dot_permissions__pb2,
)
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import code_pb2 as google_dot_rpc_dot_code__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1b\x63halk/server/v1/audit.proto\x12\x0f\x63halk.server.v1\x1a\x19\x63halk/auth/v1/agent.proto\x1a\x1f\x63halk/auth/v1/permissions.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x15google/rpc/code.proto"\xe2\x04\n\x08\x41uditLog\x12*\n\x05\x61gent\x18\x01 \x01(\x0b\x32\x14.chalk.auth.v1.AgentR\x05\x61gent\x12%\n\x0b\x64\x65scription\x18\x02 \x01(\tH\x00R\x0b\x64\x65scription\x88\x01\x01\x12\x1a\n\x08\x65ndpoint\x18\x03 \x01(\tR\x08\x65ndpoint\x12*\n\x02\x61t\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x02\x61t\x12\x1e\n\x08trace_id\x18\x05 \x01(\x04H\x01R\x07traceId\x88\x01\x01\x12)\n\x04\x63ode\x18\x06 \x01(\x0e\x32\x10.google.rpc.CodeH\x02R\x04\x63ode\x88\x01\x01\x12@\n\x07request\x18\x07 \x03(\x0b\x32&.chalk.server.v1.AuditLog.RequestEntryR\x07request\x12\x43\n\x08response\x18\x08 \x03(\x0b\x32\'.chalk.server.v1.AuditLog.ResponseEntryR\x08response\x12\x13\n\x02ip\x18\t \x01(\tH\x03R\x02ip\x88\x01\x01\x1aR\n\x0cRequestEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\x1aS\n\rResponseEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\x42\x0e\n\x0c_descriptionB\x0b\n\t_trace_idB\x07\n\x05_codeB\x05\n\x03_ip"\x15\n\x13GetAuditLogsRequest"E\n\x14GetAuditLogsResponse\x12-\n\x04logs\x18\x01 \x03(\x0b\x32\x19.chalk.server.v1.AuditLogR\x04logs2p\n\x0c\x41uditService\x12`\n\x0cGetAuditLogs\x12$.chalk.server.v1.GetAuditLogsRequest\x1a%.chalk.server.v1.GetAuditLogsResponse"\x03\x80}\x06\x42\x93\x01\n\x13\x63om.chalk.server.v1B\nAuditProtoP\x01Z\x12server/v1;serverv1\xa2\x02\x03\x43SX\xaa\x02\x0f\x43halk.Server.V1\xca\x02\x0f\x43halk\\Server\\V1\xe2\x02\x1b\x43halk\\Server\\V1\\GPBMetadata\xea\x02\x11\x43halk::Server::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "chalk.server.v1.audit_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n\023com.chalk.server.v1B\nAuditProtoP\001Z\022server/v1;serverv1\242\002\003CSX\252\002\017Chalk.Server.V1\312\002\017Chalk\\Server\\V1\342\002\033Chalk\\Server\\V1\\GPBMetadata\352\002\021Chalk::Server::V1"
    _globals["_AUDITLOG_REQUESTENTRY"]._options = None
    _globals["_AUDITLOG_REQUESTENTRY"]._serialized_options = b"8\001"
    _globals["_AUDITLOG_RESPONSEENTRY"]._options = None
    _globals["_AUDITLOG_RESPONSEENTRY"]._serialized_options = b"8\001"
    _globals["_AUDITSERVICE"].methods_by_name["GetAuditLogs"]._options = None
    _globals["_AUDITSERVICE"].methods_by_name[
        "GetAuditLogs"
    ]._serialized_options = b"\200}\006"
    _globals["_AUDITLOG"]._serialized_start = 195
    _globals["_AUDITLOG"]._serialized_end = 805
    _globals["_AUDITLOG_REQUESTENTRY"]._serialized_start = 593
    _globals["_AUDITLOG_REQUESTENTRY"]._serialized_end = 675
    _globals["_AUDITLOG_RESPONSEENTRY"]._serialized_start = 677
    _globals["_AUDITLOG_RESPONSEENTRY"]._serialized_end = 760
    _globals["_GETAUDITLOGSREQUEST"]._serialized_start = 807
    _globals["_GETAUDITLOGSREQUEST"]._serialized_end = 828
    _globals["_GETAUDITLOGSRESPONSE"]._serialized_start = 830
    _globals["_GETAUDITLOGSRESPONSE"]._serialized_end = 899
    _globals["_AUDITSERVICE"]._serialized_start = 901
    _globals["_AUDITSERVICE"]._serialized_end = 1013
# @@protoc_insertion_point(module_scope)
