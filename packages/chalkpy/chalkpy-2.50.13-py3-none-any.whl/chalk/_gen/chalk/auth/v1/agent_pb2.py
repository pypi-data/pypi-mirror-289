# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chalk/auth/v1/agent.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chalk._gen.chalk.auth.v1 import (
    featurepermission_pb2 as chalk_dot_auth_dot_v1_dot_featurepermission__pb2,
)
from chalk._gen.chalk.auth.v1 import (
    permissions_pb2 as chalk_dot_auth_dot_v1_dot_permissions__pb2,
)


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x19\x63halk/auth/v1/agent.proto\x12\rchalk.auth.v1\x1a%chalk/auth/v1/featurepermission.proto\x1a\x1f\x63halk/auth/v1/permissions.proto"\xa9\x01\n\x16\x45nvironmentPermissions\x12;\n\x0bpermissions\x18\x02 \x03(\x0e\x32\x19.chalk.auth.v1.PermissionR\x0bpermissions\x12R\n\x13\x66\x65\x61ture_permissions\x18\x03 \x01(\x0b\x32!.chalk.auth.v1.FeaturePermissionsR\x12\x66\x65\x61turePermissions"\xec\x02\n\tUserAgent\x12\x1f\n\tclient_id\x18\x01 \x01(\tB\x02\x18\x01R\x08\x63lientId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12\x17\n\x07team_id\x18\x03 \x01(\tR\x06teamId\x12t\n\x1apermissions_by_environment\x18\x04 \x03(\x0b\x32\x36.chalk.auth.v1.UserAgent.PermissionsByEnvironmentEntryR\x18permissionsByEnvironment\x12"\n\x0cimpersonated\x18\x05 \x01(\x08R\x0cimpersonated\x1ar\n\x1dPermissionsByEnvironmentEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12;\n\x05value\x18\x02 \x01(\x0b\x32%.chalk.auth.v1.EnvironmentPermissionsR\x05value:\x02\x38\x01"7\n\x0b\x43ustomClaim\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x16\n\x06values\x18\x02 \x03(\tR\x06values"\xfa\x02\n\x11ServiceTokenAgent\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1b\n\tclient_id\x18\x02 \x01(\tR\x08\x63lientId\x12\x17\n\x07team_id\x18\x03 \x01(\tR\x06teamId\x12 \n\x0b\x65nvironment\x18\x04 \x01(\tR\x0b\x65nvironment\x12;\n\x0bpermissions\x18\x05 \x03(\x0e\x32\x19.chalk.auth.v1.PermissionR\x0bpermissions\x12\'\n\rcustom_claims\x18\x06 \x03(\tB\x02\x18\x01R\x0c\x63ustomClaims\x12\x43\n\x0f\x63ustomer_claims\x18\x07 \x03(\x0b\x32\x1a.chalk.auth.v1.CustomClaimR\x0e\x63ustomerClaims\x12R\n\x13\x66\x65\x61ture_permissions\x18\x08 \x01(\x0b\x32!.chalk.auth.v1.FeaturePermissionsR\x12\x66\x65\x61turePermissions"\xa0\x01\n\x0b\x45ngineAgent\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x17\n\x07team_id\x18\x02 \x01(\tR\x06teamId\x12\x1d\n\nproject_id\x18\x03 \x01(\tR\tprojectId\x12%\n\x0e\x65nvironment_id\x18\x04 \x01(\tR\renvironmentId\x12"\n\x0cimpersonated\x18\x05 \x01(\x08R\x0cimpersonated"\x16\n\x14MetadataServiceAgent"\r\n\x0bTenantAgent"\xfe\x02\n\x05\x41gent\x12\x39\n\nuser_agent\x18\x01 \x01(\x0b\x32\x18.chalk.auth.v1.UserAgentH\x00R\tuserAgent\x12R\n\x13service_token_agent\x18\x02 \x01(\x0b\x32 .chalk.auth.v1.ServiceTokenAgentH\x00R\x11serviceTokenAgent\x12?\n\x0c\x65ngine_agent\x18\x03 \x01(\x0b\x32\x1a.chalk.auth.v1.EngineAgentH\x00R\x0b\x65ngineAgent\x12?\n\x0ctenant_agent\x18\x04 \x01(\x0b\x32\x1a.chalk.auth.v1.TenantAgentH\x00R\x0btenantAgent\x12[\n\x16metadata_service_agent\x18\x05 \x01(\x0b\x32#.chalk.auth.v1.MetadataServiceAgentH\x00R\x14metadataServiceAgentB\x07\n\x05\x61gentB\x85\x01\n\x11\x63om.chalk.auth.v1B\nAgentProtoP\x01Z\x0e\x61uth/v1;authv1\xa2\x02\x03\x43\x41X\xaa\x02\rChalk.Auth.V1\xca\x02\rChalk\\Auth\\V1\xe2\x02\x19\x43halk\\Auth\\V1\\GPBMetadata\xea\x02\x0f\x43halk::Auth::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "chalk.auth.v1.agent_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n\021com.chalk.auth.v1B\nAgentProtoP\001Z\016auth/v1;authv1\242\002\003CAX\252\002\rChalk.Auth.V1\312\002\rChalk\\Auth\\V1\342\002\031Chalk\\Auth\\V1\\GPBMetadata\352\002\017Chalk::Auth::V1"
    _globals["_USERAGENT_PERMISSIONSBYENVIRONMENTENTRY"]._options = None
    _globals["_USERAGENT_PERMISSIONSBYENVIRONMENTENTRY"]._serialized_options = b"8\001"
    _globals["_USERAGENT"].fields_by_name["client_id"]._options = None
    _globals["_USERAGENT"].fields_by_name["client_id"]._serialized_options = b"\030\001"
    _globals["_SERVICETOKENAGENT"].fields_by_name["custom_claims"]._options = None
    _globals["_SERVICETOKENAGENT"].fields_by_name[
        "custom_claims"
    ]._serialized_options = b"\030\001"
    _globals["_ENVIRONMENTPERMISSIONS"]._serialized_start = 117
    _globals["_ENVIRONMENTPERMISSIONS"]._serialized_end = 286
    _globals["_USERAGENT"]._serialized_start = 289
    _globals["_USERAGENT"]._serialized_end = 653
    _globals["_USERAGENT_PERMISSIONSBYENVIRONMENTENTRY"]._serialized_start = 539
    _globals["_USERAGENT_PERMISSIONSBYENVIRONMENTENTRY"]._serialized_end = 653
    _globals["_CUSTOMCLAIM"]._serialized_start = 655
    _globals["_CUSTOMCLAIM"]._serialized_end = 710
    _globals["_SERVICETOKENAGENT"]._serialized_start = 713
    _globals["_SERVICETOKENAGENT"]._serialized_end = 1091
    _globals["_ENGINEAGENT"]._serialized_start = 1094
    _globals["_ENGINEAGENT"]._serialized_end = 1254
    _globals["_METADATASERVICEAGENT"]._serialized_start = 1256
    _globals["_METADATASERVICEAGENT"]._serialized_end = 1278
    _globals["_TENANTAGENT"]._serialized_start = 1280
    _globals["_TENANTAGENT"]._serialized_end = 1293
    _globals["_AGENT"]._serialized_start = 1296
    _globals["_AGENT"]._serialized_end = 1678
# @@protoc_insertion_point(module_scope)
