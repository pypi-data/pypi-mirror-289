# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chalk/common/v1/chalk_error.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n!chalk/common/v1/chalk_error.proto\x12\x0f\x63halk.common.v1"\x8f\x01\n\x0e\x43halkException\x12\x12\n\x04kind\x18\x01 \x01(\tR\x04kind\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x1e\n\nstacktrace\x18\x03 \x01(\tR\nstacktrace\x12/\n\x13internal_stacktrace\x18\x04 \x01(\tR\x12internalStacktrace"\xe6\x03\n\nChalkError\x12.\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x1a.chalk.common.v1.ErrorCodeR\x04\x63ode\x12>\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32".chalk.common.v1.ErrorCodeCategoryR\x08\x63\x61tegory\x12\x18\n\x07message\x18\x03 \x01(\tR\x07message\x12\x33\n\x13\x64isplay_primary_key\x18\x65 \x01(\tH\x00R\x11\x64isplayPrimaryKey\x88\x01\x01\x12:\n\x17\x64isplay_primary_key_fqn\x18\x66 \x01(\tH\x01R\x14\x64isplayPrimaryKeyFqn\x88\x01\x01\x12\x42\n\texception\x18g \x01(\x0b\x32\x1f.chalk.common.v1.ChalkExceptionH\x02R\texception\x88\x01\x01\x12\x1d\n\x07\x66\x65\x61ture\x18h \x01(\tH\x03R\x07\x66\x65\x61ture\x88\x01\x01\x12\x1f\n\x08resolver\x18i \x01(\tH\x04R\x08resolver\x88\x01\x01\x42\x16\n\x14_display_primary_keyB\x1a\n\x18_display_primary_key_fqnB\x0c\n\n_exceptionB\n\n\x08_featureB\x0b\n\t_resolver*\x99\x03\n\tErrorCode\x12\x30\n,ERROR_CODE_INTERNAL_SERVER_ERROR_UNSPECIFIED\x10\x00\x12\x1b\n\x17\x45RROR_CODE_PARSE_FAILED\x10\x01\x12!\n\x1d\x45RROR_CODE_RESOLVER_NOT_FOUND\x10\x02\x12\x1c\n\x18\x45RROR_CODE_INVALID_QUERY\x10\x03\x12 \n\x1c\x45RROR_CODE_VALIDATION_FAILED\x10\x04\x12\x1e\n\x1a\x45RROR_CODE_RESOLVER_FAILED\x10\x05\x12!\n\x1d\x45RROR_CODE_RESOLVER_TIMED_OUT\x10\x06\x12\x1e\n\x1a\x45RROR_CODE_UPSTREAM_FAILED\x10\x07\x12\x1e\n\x1a\x45RROR_CODE_UNAUTHENTICATED\x10\x08\x12\x1b\n\x17\x45RROR_CODE_UNAUTHORIZED\x10\t\x12\x18\n\x14\x45RROR_CODE_CANCELLED\x10\n\x12 \n\x1c\x45RROR_CODE_DEADLINE_EXCEEDED\x10\x0b*\x80\x01\n\x11\x45rrorCodeCategory\x12+\n\'ERROR_CODE_CATEGORY_NETWORK_UNSPECIFIED\x10\x00\x12\x1f\n\x1b\x45RROR_CODE_CATEGORY_REQUEST\x10\x01\x12\x1d\n\x19\x45RROR_CODE_CATEGORY_FIELD\x10\x02\x42\x84\x01\n\x13\x63om.chalk.common.v1B\x0f\x43halkErrorProtoP\x01\xa2\x02\x03\x43\x43X\xaa\x02\x0f\x43halk.Common.V1\xca\x02\x0f\x43halk\\Common\\V1\xe2\x02\x1b\x43halk\\Common\\V1\\GPBMetadata\xea\x02\x11\x43halk::Common::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "chalk.common.v1.chalk_error_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n\023com.chalk.common.v1B\017ChalkErrorProtoP\001\242\002\003CCX\252\002\017Chalk.Common.V1\312\002\017Chalk\\Common\\V1\342\002\033Chalk\\Common\\V1\\GPBMetadata\352\002\021Chalk::Common::V1"
    _globals["_ERRORCODE"]._serialized_start = 690
    _globals["_ERRORCODE"]._serialized_end = 1099
    _globals["_ERRORCODECATEGORY"]._serialized_start = 1102
    _globals["_ERRORCODECATEGORY"]._serialized_end = 1230
    _globals["_CHALKEXCEPTION"]._serialized_start = 55
    _globals["_CHALKEXCEPTION"]._serialized_end = 198
    _globals["_CHALKERROR"]._serialized_start = 201
    _globals["_CHALKERROR"]._serialized_end = 687
# @@protoc_insertion_point(module_scope)
