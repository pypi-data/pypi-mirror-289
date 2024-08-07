# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chalk/common/v1/online_query.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chalk._gen.chalk.common.v1 import (
    chalk_error_pb2 as chalk_dot_common_dot_v1_dot_chalk__error__pb2,
)
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n"chalk/common/v1/online_query.proto\x12\x0f\x63halk.common.v1\x1a!chalk/common/v1/chalk_error.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc9\x04\n\x12OnlineQueryRequest\x12G\n\x06inputs\x18\x01 \x03(\x0b\x32/.chalk.common.v1.OnlineQueryRequest.InputsEntryR\x06inputs\x12\x35\n\x07outputs\x18\x02 \x03(\x0b\x32\x1b.chalk.common.v1.OutputExprR\x07outputs\x12\x31\n\x03now\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R\x03now\x88\x01\x01\x12P\n\tstaleness\x18\x04 \x03(\x0b\x32\x32.chalk.common.v1.OnlineQueryRequest.StalenessEntryR\tstaleness\x12=\n\x07\x63ontext\x18\x05 \x01(\x0b\x32#.chalk.common.v1.OnlineQueryContextR\x07\x63ontext\x12V\n\x10response_options\x18\x06 \x01(\x0b\x32+.chalk.common.v1.OnlineQueryResponseOptionsR\x0fresponseOptions\x1aQ\n\x0bInputsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\x1a<\n\x0eStalenessEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x06\n\x04_now"\x8e\x04\n\x16OnlineQueryBulkRequest\x12%\n\x0einputs_feather\x18\x01 \x01(\x0cR\rinputsFeather\x12\x35\n\x07outputs\x18\x02 \x03(\x0b\x32\x1b.chalk.common.v1.OutputExprR\x07outputs\x12,\n\x03now\x18\x03 \x03(\x0b\x32\x1a.google.protobuf.TimestampR\x03now\x12T\n\tstaleness\x18\x04 \x03(\x0b\x32\x36.chalk.common.v1.OnlineQueryBulkRequest.StalenessEntryR\tstaleness\x12=\n\x07\x63ontext\x18\x05 \x01(\x0b\x32#.chalk.common.v1.OnlineQueryContextR\x07\x63ontext\x12V\n\x10response_options\x18\x06 \x01(\x0b\x32+.chalk.common.v1.OnlineQueryResponseOptionsR\x0fresponseOptions\x12=\n\tbody_type\x18\x07 \x01(\x0e\x32 .chalk.common.v1.FeatherBodyTypeR\x08\x62odyType\x1a<\n\x0eStalenessEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01"\xb9\x01\n\x12GenericSingleQuery\x12L\n\x0esingle_request\x18\x01 \x01(\x0b\x32#.chalk.common.v1.OnlineQueryRequestH\x00R\rsingleRequest\x12L\n\x0c\x62ulk_request\x18\x02 \x01(\x0b\x32\'.chalk.common.v1.OnlineQueryBulkRequestH\x00R\x0b\x62ulkRequestB\x07\n\x05query"X\n\x17OnlineQueryMultiRequest\x12=\n\x07queries\x18\x01 \x03(\x0b\x32#.chalk.common.v1.GenericSingleQueryR\x07queries"7\n\nOutputExpr\x12!\n\x0b\x66\x65\x61ture_fqn\x18\x01 \x01(\tH\x00R\nfeatureFqnB\x06\n\x04\x65xpr"\xc8\x04\n\x12OnlineQueryContext\x12 \n\x0b\x65nvironment\x18\x01 \x01(\tR\x0b\x65nvironment\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tags\x12\x34\n\x16required_resolver_tags\x18\x03 \x03(\tR\x14requiredResolverTags\x12(\n\rdeployment_id\x18\x04 \x01(\tH\x00R\x0c\x64\x65ploymentId\x88\x01\x01\x12 \n\tbranch_id\x18\x05 \x01(\tH\x01R\x08\x62ranchId\x88\x01\x01\x12*\n\x0e\x63orrelation_id\x18\x06 \x01(\tH\x02R\rcorrelationId\x88\x01\x01\x12"\n\nquery_name\x18\x07 \x01(\tH\x03R\tqueryName\x88\x01\x01\x12\x31\n\x12query_name_version\x18\x08 \x01(\tH\x04R\x10queryNameVersion\x88\x01\x01\x12J\n\x07options\x18\t \x03(\x0b\x32\x30.chalk.common.v1.OnlineQueryContext.OptionsEntryR\x07options\x1aR\n\x0cOptionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\x42\x10\n\x0e_deployment_idB\x0c\n\n_branch_idB\x11\n\x0f_correlation_idB\r\n\x0b_query_nameB\x15\n\x13_query_name_version"\xe2\x02\n\x1aOnlineQueryResponseOptions\x12!\n\x0cinclude_meta\x18\x01 \x01(\x08R\x0bincludeMeta\x12\x39\n\x07\x65xplain\x18\x02 \x01(\x0b\x32\x1f.chalk.common.v1.ExplainOptionsR\x07\x65xplain\x12R\n\x10\x65ncoding_options\x18\x03 \x01(\x0b\x32\'.chalk.common.v1.FeatureEncodingOptionsR\x0f\x65ncodingOptions\x12U\n\x08metadata\x18\x04 \x03(\x0b\x32\x39.chalk.common.v1.OnlineQueryResponseOptions.MetadataEntryR\x08metadata\x1a;\n\rMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01"\x10\n\x0e\x45xplainOptions"S\n\x16\x46\x65\x61tureEncodingOptions\x12\x39\n\x19\x65ncode_structs_as_objects\x18\x01 \x01(\x08R\x16\x65ncodeStructsAsObjects"\xcd\x01\n\x13OnlineQueryResponse\x12\x36\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32".chalk.common.v1.OnlineQueryResultR\x04\x64\x61ta\x12\x33\n\x06\x65rrors\x18\x02 \x03(\x0b\x32\x1b.chalk.common.v1.ChalkErrorR\x06\x65rrors\x12I\n\rresponse_meta\x18\x03 \x01(\x0b\x32$.chalk.common.v1.OnlineQueryMetadataR\x0cresponseMeta"\xd6\x02\n\x17OnlineQueryBulkResponse\x12!\n\x0cscalars_data\x18\x01 \x01(\x0cR\x0bscalarsData\x12Y\n\x0bgroups_data\x18\x02 \x03(\x0b\x32\x38.chalk.common.v1.OnlineQueryBulkResponse.GroupsDataEntryR\ngroupsData\x12\x33\n\x06\x65rrors\x18\x03 \x03(\x0b\x32\x1b.chalk.common.v1.ChalkErrorR\x06\x65rrors\x12I\n\rresponse_meta\x18\x04 \x01(\x0b\x32$.chalk.common.v1.OnlineQueryMetadataR\x0cresponseMeta\x1a=\n\x0fGroupsDataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x0cR\x05value:\x02\x38\x01"\xc2\x01\n\x15GenericSingleResponse\x12O\n\x0fsingle_response\x18\x01 \x01(\x0b\x32$.chalk.common.v1.OnlineQueryResponseH\x00R\x0esingleResponse\x12O\n\rbulk_response\x18\x02 \x01(\x0b\x32(.chalk.common.v1.OnlineQueryBulkResponseH\x00R\x0c\x62ulkResponseB\x07\n\x05query"\x95\x01\n\x18OnlineQueryMultiResponse\x12\x44\n\tresponses\x18\x01 \x03(\x0b\x32&.chalk.common.v1.GenericSingleResponseR\tresponses\x12\x33\n\x06\x65rrors\x18\x02 \x03(\x0b\x32\x1b.chalk.common.v1.ChalkErrorR\x06\x65rrors"M\n\x11OnlineQueryResult\x12\x38\n\x07results\x18\x01 \x03(\x0b\x32\x1e.chalk.common.v1.FeatureResultR\x07results"\xb9\x02\n\rFeatureResult\x12\x14\n\x05\x66ield\x18\x01 \x01(\tR\x05\x66ield\x12*\n\x04pkey\x18\x06 \x01(\x0b\x32\x16.google.protobuf.ValueR\x04pkey\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value\x12\x36\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1b.chalk.common.v1.ChalkErrorH\x00R\x05\x65rror\x88\x01\x01\x12/\n\x02ts\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01R\x02ts\x88\x01\x01\x12\x35\n\x04meta\x18\x05 \x01(\x0b\x32\x1c.chalk.common.v1.FeatureMetaH\x02R\x04meta\x88\x01\x01\x42\x08\n\x06_errorB\x05\n\x03_tsB\x07\n\x05_meta"\x9b\x01\n\x0b\x46\x65\x61tureMeta\x12.\n\x13\x63hosen_resolver_fqn\x18\x01 \x01(\tR\x11\x63hosenResolverFqn\x12\x1b\n\tcache_hit\x18\x02 \x01(\x08R\x08\x63\x61\x63heHit\x12%\n\x0eprimitive_type\x18\x03 \x01(\tR\rprimitiveType\x12\x18\n\x07version\x18\x04 \x01(\x03R\x07version"\xac\x04\n\x13OnlineQueryMetadata\x12H\n\x12\x65xecution_duration\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x11\x65xecutionDuration\x12#\n\rdeployment_id\x18\x02 \x01(\tR\x0c\x64\x65ploymentId\x12%\n\x0e\x65nvironment_id\x18\x03 \x01(\tR\renvironmentId\x12)\n\x10\x65nvironment_name\x18\x04 \x01(\tR\x0f\x65nvironmentName\x12\x19\n\x08query_id\x18\x05 \x01(\tR\x07queryId\x12\x43\n\x0fquery_timestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0equeryTimestamp\x12\x1d\n\nquery_hash\x18\x07 \x01(\tR\tqueryHash\x12H\n\x0e\x65xplain_output\x18\x08 \x01(\x0b\x32!.chalk.common.v1.QueryExplainInfoR\rexplainOutput\x12N\n\x08metadata\x18\t \x03(\x0b\x32\x32.chalk.common.v1.OnlineQueryMetadata.MetadataEntryR\x08metadata\x1a;\n\rMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01"H\n\x10QueryExplainInfo\x12$\n\x0bplan_string\x18\x01 \x01(\tH\x00R\nplanString\x88\x01\x01\x42\x0e\n\x0c_plan_string"\x81\x01\n\x19UploadFeaturesBulkRequest\x12%\n\x0einputs_feather\x18\x01 \x01(\x0cR\rinputsFeather\x12=\n\tbody_type\x18\x07 \x01(\x0e\x32 .chalk.common.v1.FeatherBodyTypeR\x08\x62odyType"Q\n\x1aUploadFeaturesBulkResponse\x12\x33\n\x06\x65rrors\x18\x01 \x03(\x0b\x32\x1b.chalk.common.v1.ChalkErrorR\x06\x65rrors*w\n\x0f\x46\x65\x61therBodyType\x12!\n\x1d\x46\x45\x41THER_BODY_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17\x46\x45\x41THER_BODY_TYPE_TABLE\x10\x01\x12$\n FEATHER_BODY_TYPE_RECORD_BATCHES\x10\x02\x42\x85\x01\n\x13\x63om.chalk.common.v1B\x10OnlineQueryProtoP\x01\xa2\x02\x03\x43\x43X\xaa\x02\x0f\x43halk.Common.V1\xca\x02\x0f\x43halk\\Common\\V1\xe2\x02\x1b\x43halk\\Common\\V1\\GPBMetadata\xea\x02\x11\x43halk::Common::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "chalk.common.v1.online_query_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n\023com.chalk.common.v1B\020OnlineQueryProtoP\001\242\002\003CCX\252\002\017Chalk.Common.V1\312\002\017Chalk\\Common\\V1\342\002\033Chalk\\Common\\V1\\GPBMetadata\352\002\021Chalk::Common::V1"
    _globals["_ONLINEQUERYREQUEST_INPUTSENTRY"]._options = None
    _globals["_ONLINEQUERYREQUEST_INPUTSENTRY"]._serialized_options = b"8\001"
    _globals["_ONLINEQUERYREQUEST_STALENESSENTRY"]._options = None
    _globals["_ONLINEQUERYREQUEST_STALENESSENTRY"]._serialized_options = b"8\001"
    _globals["_ONLINEQUERYBULKREQUEST_STALENESSENTRY"]._options = None
    _globals["_ONLINEQUERYBULKREQUEST_STALENESSENTRY"]._serialized_options = b"8\001"
    _globals["_ONLINEQUERYCONTEXT_OPTIONSENTRY"]._options = None
    _globals["_ONLINEQUERYCONTEXT_OPTIONSENTRY"]._serialized_options = b"8\001"
    _globals["_ONLINEQUERYRESPONSEOPTIONS_METADATAENTRY"]._options = None
    _globals["_ONLINEQUERYRESPONSEOPTIONS_METADATAENTRY"]._serialized_options = b"8\001"
    _globals["_ONLINEQUERYBULKRESPONSE_GROUPSDATAENTRY"]._options = None
    _globals["_ONLINEQUERYBULKRESPONSE_GROUPSDATAENTRY"]._serialized_options = b"8\001"
    _globals["_ONLINEQUERYMETADATA_METADATAENTRY"]._options = None
    _globals["_ONLINEQUERYMETADATA_METADATAENTRY"]._serialized_options = b"8\001"
    _globals["_FEATHERBODYTYPE"]._serialized_start = 4987
    _globals["_FEATHERBODYTYPE"]._serialized_end = 5106
    _globals["_ONLINEQUERYREQUEST"]._serialized_start = 186
    _globals["_ONLINEQUERYREQUEST"]._serialized_end = 771
    _globals["_ONLINEQUERYREQUEST_INPUTSENTRY"]._serialized_start = 620
    _globals["_ONLINEQUERYREQUEST_INPUTSENTRY"]._serialized_end = 701
    _globals["_ONLINEQUERYREQUEST_STALENESSENTRY"]._serialized_start = 703
    _globals["_ONLINEQUERYREQUEST_STALENESSENTRY"]._serialized_end = 763
    _globals["_ONLINEQUERYBULKREQUEST"]._serialized_start = 774
    _globals["_ONLINEQUERYBULKREQUEST"]._serialized_end = 1300
    _globals["_ONLINEQUERYBULKREQUEST_STALENESSENTRY"]._serialized_start = 703
    _globals["_ONLINEQUERYBULKREQUEST_STALENESSENTRY"]._serialized_end = 763
    _globals["_GENERICSINGLEQUERY"]._serialized_start = 1303
    _globals["_GENERICSINGLEQUERY"]._serialized_end = 1488
    _globals["_ONLINEQUERYMULTIREQUEST"]._serialized_start = 1490
    _globals["_ONLINEQUERYMULTIREQUEST"]._serialized_end = 1578
    _globals["_OUTPUTEXPR"]._serialized_start = 1580
    _globals["_OUTPUTEXPR"]._serialized_end = 1635
    _globals["_ONLINEQUERYCONTEXT"]._serialized_start = 1638
    _globals["_ONLINEQUERYCONTEXT"]._serialized_end = 2222
    _globals["_ONLINEQUERYCONTEXT_OPTIONSENTRY"]._serialized_start = 2051
    _globals["_ONLINEQUERYCONTEXT_OPTIONSENTRY"]._serialized_end = 2133
    _globals["_ONLINEQUERYRESPONSEOPTIONS"]._serialized_start = 2225
    _globals["_ONLINEQUERYRESPONSEOPTIONS"]._serialized_end = 2579
    _globals["_ONLINEQUERYRESPONSEOPTIONS_METADATAENTRY"]._serialized_start = 2520
    _globals["_ONLINEQUERYRESPONSEOPTIONS_METADATAENTRY"]._serialized_end = 2579
    _globals["_EXPLAINOPTIONS"]._serialized_start = 2581
    _globals["_EXPLAINOPTIONS"]._serialized_end = 2597
    _globals["_FEATUREENCODINGOPTIONS"]._serialized_start = 2599
    _globals["_FEATUREENCODINGOPTIONS"]._serialized_end = 2682
    _globals["_ONLINEQUERYRESPONSE"]._serialized_start = 2685
    _globals["_ONLINEQUERYRESPONSE"]._serialized_end = 2890
    _globals["_ONLINEQUERYBULKRESPONSE"]._serialized_start = 2893
    _globals["_ONLINEQUERYBULKRESPONSE"]._serialized_end = 3235
    _globals["_ONLINEQUERYBULKRESPONSE_GROUPSDATAENTRY"]._serialized_start = 3174
    _globals["_ONLINEQUERYBULKRESPONSE_GROUPSDATAENTRY"]._serialized_end = 3235
    _globals["_GENERICSINGLERESPONSE"]._serialized_start = 3238
    _globals["_GENERICSINGLERESPONSE"]._serialized_end = 3432
    _globals["_ONLINEQUERYMULTIRESPONSE"]._serialized_start = 3435
    _globals["_ONLINEQUERYMULTIRESPONSE"]._serialized_end = 3584
    _globals["_ONLINEQUERYRESULT"]._serialized_start = 3586
    _globals["_ONLINEQUERYRESULT"]._serialized_end = 3663
    _globals["_FEATURERESULT"]._serialized_start = 3666
    _globals["_FEATURERESULT"]._serialized_end = 3979
    _globals["_FEATUREMETA"]._serialized_start = 3982
    _globals["_FEATUREMETA"]._serialized_end = 4137
    _globals["_ONLINEQUERYMETADATA"]._serialized_start = 4140
    _globals["_ONLINEQUERYMETADATA"]._serialized_end = 4696
    _globals["_ONLINEQUERYMETADATA_METADATAENTRY"]._serialized_start = 2520
    _globals["_ONLINEQUERYMETADATA_METADATAENTRY"]._serialized_end = 2579
    _globals["_QUERYEXPLAININFO"]._serialized_start = 4698
    _globals["_QUERYEXPLAININFO"]._serialized_end = 4770
    _globals["_UPLOADFEATURESBULKREQUEST"]._serialized_start = 4773
    _globals["_UPLOADFEATURESBULKREQUEST"]._serialized_end = 4902
    _globals["_UPLOADFEATURESBULKRESPONSE"]._serialized_start = 4904
    _globals["_UPLOADFEATURESBULKRESPONSE"]._serialized_end = 4985
# @@protoc_insertion_point(module_scope)
