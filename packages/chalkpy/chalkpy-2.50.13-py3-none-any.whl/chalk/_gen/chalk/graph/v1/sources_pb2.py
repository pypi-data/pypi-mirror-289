# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chalk/graph/v1/sources.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chalk._gen.chalk.arrow.v1 import arrow_pb2 as chalk_dot_arrow_dot_v1_dot_arrow__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1c\x63halk/graph/v1/sources.proto\x12\x0e\x63halk.graph.v1\x1a\x1a\x63halk/arrow/v1/arrow.proto\x1a\x1egoogle/protobuf/duration.proto"a\n\x15StreamSourceReference\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32 .chalk.graph.v1.StreamSourceTypeR\x04type\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name"\xc0\x01\n\x0cStreamSource\x12\x33\n\x05kafka\x18\x01 \x01(\x0b\x32\x1b.chalk.graph.v1.KafkaSourceH\x00R\x05kafka\x12\x39\n\x07kinesis\x18\x02 \x01(\x0b\x32\x1d.chalk.graph.v1.KinesisSourceH\x00R\x07kinesis\x12\x36\n\x06pubsub\x18\x03 \x01(\x0b\x32\x1c.chalk.graph.v1.PubSubSourceH\x00R\x06pubsubB\x08\n\x06source"\xee\x03\n\rKinesisSource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0bstream_name\x18\x02 \x01(\tR\nstreamName\x12\x1d\n\nstream_arn\x18\x03 \x01(\tR\tstreamArn\x12\x1f\n\x0bregion_name\x18\x04 \x01(\tR\nregionName\x12M\n\x15late_arrival_deadline\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationR\x13lateArrivalDeadline\x12@\n\x1d\x64\x65\x61\x64_letter_queue_stream_name\x18\x06 \x01(\tR\x19\x64\x65\x61\x64LetterQueueStreamName\x12)\n\x11\x61ws_access_key_id\x18\x07 \x01(\tR\x0e\x61wsAccessKeyId\x12\x31\n\x15\x61ws_secret_access_key\x18\x08 \x01(\tR\x12\x61wsSecretAccessKey\x12*\n\x11\x61ws_session_token\x18\t \x01(\tR\x0f\x61wsSessionToken\x12!\n\x0c\x65ndpoint_url\x18\n \x01(\tR\x0b\x65ndpointUrl\x12*\n\x11\x63onsumer_role_arn\x18\x0b \x01(\tR\x0f\x63onsumerRoleArn"\xae\x04\n\x0bKafkaSource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12+\n\x11\x62ootstrap_servers\x18\x02 \x03(\tR\x10\x62ootstrapServers\x12\x14\n\x05topic\x18\x03 \x01(\tR\x05topic\x12\x32\n\x15ssl_keystore_location\x18\x04 \x01(\tR\x13sslKeystoreLocation\x12\x1e\n\x0bssl_ca_file\x18\x05 \x01(\tR\tsslCaFile\x12(\n\x10\x63lient_id_prefix\x18\x06 \x01(\tR\x0e\x63lientIdPrefix\x12&\n\x0fgroup_id_prefix\x18\x07 \x01(\tR\rgroupIdPrefix\x12+\n\x11security_protocol\x18\x08 \x01(\tR\x10securityProtocol\x12%\n\x0esasl_mechanism\x18\t \x01(\tR\rsaslMechanism\x12#\n\rsasl_username\x18\n \x01(\tR\x0csaslUsername\x12#\n\rsasl_password\x18\x0b \x01(\tR\x0csaslPassword\x12M\n\x15late_arrival_deadline\x18\x0c \x01(\x0b\x32\x19.google.protobuf.DurationR\x13lateArrivalDeadline\x12\x35\n\x17\x64\x65\x61\x64_letter_queue_topic\x18\r \x01(\tR\x14\x64\x65\x61\x64LetterQueueTopic"\xf0\x01\n\x0cPubSubSource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\nproject_id\x18\x02 \x01(\tR\tprojectId\x12\'\n\x0fsubscription_id\x18\x03 \x01(\tR\x0esubscriptionId\x12M\n\x15late_arrival_deadline\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x13lateArrivalDeadline\x12\x35\n\x17\x64\x65\x61\x64_letter_queue_topic\x18\x05 \x01(\tR\x14\x64\x65\x61\x64LetterQueueTopic"e\n\x17\x44\x61tabaseSourceReference\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32".chalk.graph.v1.DatabaseSourceTypeR\x04type\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name"\xb2\x05\n\x0e\x44\x61tabaseSource\x12<\n\x08\x62igquery\x18\x01 \x01(\x0b\x32\x1e.chalk.graph.v1.BigQuerySourceH\x00R\x08\x62igquery\x12<\n\x08\x63loudsql\x18\x02 \x01(\x0b\x32\x1e.chalk.graph.v1.CloudSQLSourceH\x00R\x08\x63loudsql\x12\x42\n\ndatabricks\x18\x03 \x01(\x0b\x32 .chalk.graph.v1.DatabricksSourceH\x00R\ndatabricks\x12\x33\n\x05mysql\x18\x04 \x01(\x0b\x32\x1b.chalk.graph.v1.MySQLSourceH\x00R\x05mysql\x12<\n\x08postgres\x18\x05 \x01(\x0b\x32\x1e.chalk.graph.v1.PostgresSourceH\x00R\x08postgres\x12<\n\x08redshift\x18\x06 \x01(\x0b\x32\x1e.chalk.graph.v1.RedshiftSourceH\x00R\x08redshift\x12?\n\tsnowflake\x18\x07 \x01(\x0b\x32\x1f.chalk.graph.v1.SnowflakeSourceH\x00R\tsnowflake\x12\x36\n\x06sqlite\x18\x08 \x01(\x0b\x32\x1c.chalk.graph.v1.SQLiteSourceH\x00R\x06sqlite\x12\x39\n\x07spanner\x18\t \x01(\x0b\x32\x1d.chalk.graph.v1.SpannerSourceH\x00R\x07spanner\x12\x33\n\x05trino\x18\n \x01(\x0b\x32\x1b.chalk.graph.v1.TrinoSourceH\x00R\x05trino\x12<\n\x08\x64ynamodb\x18\x0b \x01(\x0b\x32\x1e.chalk.graph.v1.DynamoDBSourceH\x00R\x08\x64ynamodbB\x08\n\x06source"\xbd\x04\n\x0e\x42igQuerySource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07project\x18\x02 \x01(\tR\x07project\x12\x18\n\x07\x64\x61taset\x18\x03 \x01(\tR\x07\x64\x61taset\x12\x1a\n\x08location\x18\x04 \x01(\tR\x08location\x12-\n\x12\x63redentials_base64\x18\x05 \x01(\tR\x11\x63redentialsBase64\x12)\n\x10\x63redentials_path\x18\x06 \x01(\tR\x0f\x63redentialsPath\x12O\n\x0b\x65ngine_args\x18\x07 \x03(\x0b\x32..chalk.graph.v1.BigQuerySource.EngineArgsEntryR\nengineArgs\x12_\n\x11\x61sync_engine_args\x18\x08 \x03(\x0b\x32\x33.chalk.graph.v1.BigQuerySource.AsyncEngineArgsEntryR\x0f\x61syncEngineArgs\x1aZ\n\x0f\x45ngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01\x1a_\n\x14\x41syncEngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01"\xf8\x03\n\x0e\x43loudSQLSource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x0e\n\x02\x64\x62\x18\x02 \x01(\tR\x02\x64\x62\x12\x12\n\x04user\x18\x03 \x01(\tR\x04user\x12\x1a\n\x08password\x18\x04 \x01(\tR\x08password\x12#\n\rinstance_name\x18\x05 \x01(\tR\x0cinstanceName\x12O\n\x0b\x65ngine_args\x18\x06 \x03(\x0b\x32..chalk.graph.v1.CloudSQLSource.EngineArgsEntryR\nengineArgs\x12_\n\x11\x61sync_engine_args\x18\x07 \x03(\x0b\x32\x33.chalk.graph.v1.CloudSQLSource.AsyncEngineArgsEntryR\x0f\x61syncEngineArgs\x1aZ\n\x0f\x45ngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01\x1a_\n\x14\x41syncEngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01"\x91\x04\n\x10\x44\x61tabricksSource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04host\x18\x02 \x01(\tR\x04host\x12\x12\n\x04port\x18\x03 \x01(\tR\x04port\x12\x0e\n\x02\x64\x62\x18\x04 \x01(\tR\x02\x64\x62\x12\x1b\n\thttp_path\x18\x05 \x01(\tR\x08httpPath\x12!\n\x0c\x61\x63\x63\x65ss_token\x18\x06 \x01(\tR\x0b\x61\x63\x63\x65ssToken\x12Q\n\x0b\x65ngine_args\x18\x07 \x03(\x0b\x32\x30.chalk.graph.v1.DatabricksSource.EngineArgsEntryR\nengineArgs\x12\x61\n\x11\x61sync_engine_args\x18\x08 \x03(\x0b\x32\x35.chalk.graph.v1.DatabricksSource.AsyncEngineArgsEntryR\x0f\x61syncEngineArgs\x1aZ\n\x0f\x45ngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01\x1a_\n\x14\x41syncEngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01"\xde\x05\n\x0e\x44ynamoDBSource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x38\n\x16\x61ws_client_id_override\x18\x02 \x01(\tH\x00R\x13\x61wsClientIdOverride\x88\x01\x01\x12@\n\x1a\x61ws_client_secret_override\x18\x03 \x01(\tH\x01R\x17\x61wsClientSecretOverride\x88\x01\x01\x12\x33\n\x13\x61ws_region_override\x18\x04 \x01(\tH\x02R\x11\x61wsRegionOverride\x88\x01\x01\x12\x30\n\x11\x65ndpoint_override\x18\x05 \x01(\tH\x03R\x10\x65ndpointOverride\x88\x01\x01\x12O\n\x0b\x65ngine_args\x18\x06 \x03(\x0b\x32..chalk.graph.v1.DynamoDBSource.EngineArgsEntryR\nengineArgs\x12_\n\x11\x61sync_engine_args\x18\x07 \x03(\x0b\x32\x33.chalk.graph.v1.DynamoDBSource.AsyncEngineArgsEntryR\x0f\x61syncEngineArgs\x1aZ\n\x0f\x45ngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01\x1a_\n\x14\x41syncEngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01\x42\x19\n\x17_aws_client_id_overrideB\x1d\n\x1b_aws_client_secret_overrideB\x16\n\x14_aws_region_overrideB\x14\n\x12_endpoint_override"\xf2\x03\n\x0bMySQLSource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04host\x18\x02 \x01(\tR\x04host\x12\x12\n\x04port\x18\x03 \x01(\tR\x04port\x12\x0e\n\x02\x64\x62\x18\x04 \x01(\tR\x02\x64\x62\x12\x12\n\x04user\x18\x05 \x01(\tR\x04user\x12\x1a\n\x08password\x18\x06 \x01(\tR\x08password\x12L\n\x0b\x65ngine_args\x18\x07 \x03(\x0b\x32+.chalk.graph.v1.MySQLSource.EngineArgsEntryR\nengineArgs\x12\\\n\x11\x61sync_engine_args\x18\x08 \x03(\x0b\x32\x30.chalk.graph.v1.MySQLSource.AsyncEngineArgsEntryR\x0f\x61syncEngineArgs\x1aZ\n\x0f\x45ngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01\x1a_\n\x14\x41syncEngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01"\xfb\x03\n\x0ePostgresSource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04host\x18\x02 \x01(\tR\x04host\x12\x12\n\x04port\x18\x03 \x01(\tR\x04port\x12\x0e\n\x02\x64\x62\x18\x04 \x01(\tR\x02\x64\x62\x12\x12\n\x04user\x18\x05 \x01(\tR\x04user\x12\x1a\n\x08password\x18\x06 \x01(\tR\x08password\x12O\n\x0b\x65ngine_args\x18\x07 \x03(\x0b\x32..chalk.graph.v1.PostgresSource.EngineArgsEntryR\nengineArgs\x12_\n\x11\x61sync_engine_args\x18\x08 \x03(\x0b\x32\x33.chalk.graph.v1.PostgresSource.AsyncEngineArgsEntryR\x0f\x61syncEngineArgs\x1aZ\n\x0f\x45ngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01\x1a_\n\x14\x41syncEngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01"\xb5\x04\n\x0eRedshiftSource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04host\x18\x02 \x01(\tR\x04host\x12\x12\n\x04port\x18\x03 \x01(\tR\x04port\x12\x0e\n\x02\x64\x62\x18\x04 \x01(\tR\x02\x64\x62\x12\x12\n\x04user\x18\x05 \x01(\tR\x04user\x12\x1a\n\x08password\x18\x06 \x01(\tR\x08password\x12\x1b\n\ts3_client\x18\x07 \x01(\tR\x08s3Client\x12\x1b\n\ts3_bucket\x18\x08 \x01(\tR\x08s3Bucket\x12O\n\x0b\x65ngine_args\x18\t \x03(\x0b\x32..chalk.graph.v1.RedshiftSource.EngineArgsEntryR\nengineArgs\x12_\n\x11\x61sync_engine_args\x18\n \x03(\x0b\x32\x33.chalk.graph.v1.RedshiftSource.AsyncEngineArgsEntryR\x0f\x61syncEngineArgs\x1aZ\n\x0f\x45ngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01\x1a_\n\x14\x41syncEngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01"\xf7\x04\n\x0fSnowflakeSource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x0e\n\x02\x64\x62\x18\x02 \x01(\tR\x02\x64\x62\x12\x16\n\x06schema\x18\x03 \x01(\tR\x06schema\x12\x12\n\x04role\x18\x04 \x01(\tR\x04role\x12\x12\n\x04user\x18\x05 \x01(\tR\x04user\x12\x1a\n\x08password\x18\x06 \x01(\tR\x08password\x12-\n\x12\x61\x63\x63ount_identifier\x18\x07 \x01(\tR\x11\x61\x63\x63ountIdentifier\x12\x1c\n\twarehouse\x18\x08 \x01(\tR\twarehouse\x12P\n\x0b\x65ngine_args\x18\t \x03(\x0b\x32/.chalk.graph.v1.SnowflakeSource.EngineArgsEntryR\nengineArgs\x12`\n\x11\x61sync_engine_args\x18\n \x03(\x0b\x32\x34.chalk.graph.v1.SnowflakeSource.AsyncEngineArgsEntryR\x0f\x61syncEngineArgs\x12&\n\x0fprivate_key_b64\x18\x0b \x01(\tR\rprivateKeyB64\x1aZ\n\x0f\x45ngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01\x1a_\n\x14\x41syncEngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01"\xaa\x03\n\x0cSQLiteSource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1b\n\tfile_name\x18\x02 \x01(\tR\x08\x66ileName\x12M\n\x0b\x65ngine_args\x18\x03 \x03(\x0b\x32,.chalk.graph.v1.SQLiteSource.EngineArgsEntryR\nengineArgs\x12]\n\x11\x61sync_engine_args\x18\x04 \x03(\x0b\x32\x31.chalk.graph.v1.SQLiteSource.AsyncEngineArgsEntryR\x0f\x61syncEngineArgs\x1aZ\n\x0f\x45ngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01\x1a_\n\x14\x41syncEngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01"\x85\x04\n\rSpannerSource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07project\x18\x02 \x01(\tR\x07project\x12\x1a\n\x08instance\x18\x03 \x01(\tR\x08instance\x12\x0e\n\x02\x64\x62\x18\x04 \x01(\tR\x02\x64\x62\x12-\n\x12\x63redentials_base64\x18\x05 \x01(\tR\x11\x63redentialsBase64\x12N\n\x0b\x65ngine_args\x18\x06 \x03(\x0b\x32-.chalk.graph.v1.SpannerSource.EngineArgsEntryR\nengineArgs\x12^\n\x11\x61sync_engine_args\x18\x07 \x03(\x0b\x32\x32.chalk.graph.v1.SpannerSource.AsyncEngineArgsEntryR\x0f\x61syncEngineArgs\x1aZ\n\x0f\x45ngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01\x1a_\n\x14\x41syncEngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01"\x94\x04\n\x0bTrinoSource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04host\x18\x02 \x01(\tR\x04host\x12\x12\n\x04port\x18\x03 \x01(\tR\x04port\x12\x18\n\x07\x63\x61talog\x18\x04 \x01(\tR\x07\x63\x61talog\x12\x16\n\x06schema\x18\x05 \x01(\tR\x06schema\x12\x12\n\x04user\x18\x06 \x01(\tR\x04user\x12\x1a\n\x08password\x18\x07 \x01(\tR\x08password\x12L\n\x0b\x65ngine_args\x18\x08 \x03(\x0b\x32+.chalk.graph.v1.TrinoSource.EngineArgsEntryR\nengineArgs\x12\\\n\x11\x61sync_engine_args\x18\t \x03(\x0b\x32\x30.chalk.graph.v1.TrinoSource.AsyncEngineArgsEntryR\x0f\x61syncEngineArgs\x1aZ\n\x0f\x45ngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01\x1a_\n\x14\x41syncEngineArgsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chalk.arrow.v1.ScalarValueR\x05value:\x02\x38\x01*\x93\x01\n\x10StreamSourceType\x12"\n\x1eSTREAM_SOURCE_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18STREAM_SOURCE_TYPE_KAFKA\x10\x01\x12\x1e\n\x1aSTREAM_SOURCE_TYPE_KINESIS\x10\x02\x12\x1d\n\x19STREAM_SOURCE_TYPE_PUBSUB\x10\x03*\xb5\x03\n\x12\x44\x61tabaseSourceType\x12$\n DATABASE_SOURCE_TYPE_UNSPECIFIED\x10\x00\x12!\n\x1d\x44\x41TABASE_SOURCE_TYPE_BIGQUERY\x10\x01\x12!\n\x1d\x44\x41TABASE_SOURCE_TYPE_CLOUDSQL\x10\x02\x12#\n\x1f\x44\x41TABASE_SOURCE_TYPE_DATABRICKS\x10\x03\x12\x1e\n\x1a\x44\x41TABASE_SOURCE_TYPE_MYSQL\x10\x04\x12!\n\x1d\x44\x41TABASE_SOURCE_TYPE_POSTGRES\x10\x05\x12!\n\x1d\x44\x41TABASE_SOURCE_TYPE_REDSHIFT\x10\x06\x12"\n\x1e\x44\x41TABASE_SOURCE_TYPE_SNOWFLAKE\x10\x07\x12\x1f\n\x1b\x44\x41TABASE_SOURCE_TYPE_SQLITE\x10\x08\x12 \n\x1c\x44\x41TABASE_SOURCE_TYPE_SPANNER\x10\t\x12\x1e\n\x1a\x44\x41TABASE_SOURCE_TYPE_TRINO\x10\n\x12!\n\x1d\x44\x41TABASE_SOURCE_TYPE_DYNAMODB\x10\x0b\x42|\n\x12\x63om.chalk.graph.v1B\x0cSourcesProtoP\x01\xa2\x02\x03\x43GX\xaa\x02\x0e\x43halk.Graph.V1\xca\x02\x0e\x43halk\\Graph\\V1\xe2\x02\x1a\x43halk\\Graph\\V1\\GPBMetadata\xea\x02\x10\x43halk::Graph::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "chalk.graph.v1.sources_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n\022com.chalk.graph.v1B\014SourcesProtoP\001\242\002\003CGX\252\002\016Chalk.Graph.V1\312\002\016Chalk\\Graph\\V1\342\002\032Chalk\\Graph\\V1\\GPBMetadata\352\002\020Chalk::Graph::V1"
    _globals["_BIGQUERYSOURCE_ENGINEARGSENTRY"]._options = None
    _globals["_BIGQUERYSOURCE_ENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_BIGQUERYSOURCE_ASYNCENGINEARGSENTRY"]._options = None
    _globals["_BIGQUERYSOURCE_ASYNCENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_CLOUDSQLSOURCE_ENGINEARGSENTRY"]._options = None
    _globals["_CLOUDSQLSOURCE_ENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_CLOUDSQLSOURCE_ASYNCENGINEARGSENTRY"]._options = None
    _globals["_CLOUDSQLSOURCE_ASYNCENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_DATABRICKSSOURCE_ENGINEARGSENTRY"]._options = None
    _globals["_DATABRICKSSOURCE_ENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_DATABRICKSSOURCE_ASYNCENGINEARGSENTRY"]._options = None
    _globals["_DATABRICKSSOURCE_ASYNCENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_DYNAMODBSOURCE_ENGINEARGSENTRY"]._options = None
    _globals["_DYNAMODBSOURCE_ENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_DYNAMODBSOURCE_ASYNCENGINEARGSENTRY"]._options = None
    _globals["_DYNAMODBSOURCE_ASYNCENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_MYSQLSOURCE_ENGINEARGSENTRY"]._options = None
    _globals["_MYSQLSOURCE_ENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_MYSQLSOURCE_ASYNCENGINEARGSENTRY"]._options = None
    _globals["_MYSQLSOURCE_ASYNCENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_POSTGRESSOURCE_ENGINEARGSENTRY"]._options = None
    _globals["_POSTGRESSOURCE_ENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_POSTGRESSOURCE_ASYNCENGINEARGSENTRY"]._options = None
    _globals["_POSTGRESSOURCE_ASYNCENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_REDSHIFTSOURCE_ENGINEARGSENTRY"]._options = None
    _globals["_REDSHIFTSOURCE_ENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_REDSHIFTSOURCE_ASYNCENGINEARGSENTRY"]._options = None
    _globals["_REDSHIFTSOURCE_ASYNCENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_SNOWFLAKESOURCE_ENGINEARGSENTRY"]._options = None
    _globals["_SNOWFLAKESOURCE_ENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_SNOWFLAKESOURCE_ASYNCENGINEARGSENTRY"]._options = None
    _globals["_SNOWFLAKESOURCE_ASYNCENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_SQLITESOURCE_ENGINEARGSENTRY"]._options = None
    _globals["_SQLITESOURCE_ENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_SQLITESOURCE_ASYNCENGINEARGSENTRY"]._options = None
    _globals["_SQLITESOURCE_ASYNCENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_SPANNERSOURCE_ENGINEARGSENTRY"]._options = None
    _globals["_SPANNERSOURCE_ENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_SPANNERSOURCE_ASYNCENGINEARGSENTRY"]._options = None
    _globals["_SPANNERSOURCE_ASYNCENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_TRINOSOURCE_ENGINEARGSENTRY"]._options = None
    _globals["_TRINOSOURCE_ENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_TRINOSOURCE_ASYNCENGINEARGSENTRY"]._options = None
    _globals["_TRINOSOURCE_ASYNCENGINEARGSENTRY"]._serialized_options = b"8\001"
    _globals["_STREAMSOURCETYPE"]._serialized_start = 8549
    _globals["_STREAMSOURCETYPE"]._serialized_end = 8696
    _globals["_DATABASESOURCETYPE"]._serialized_start = 8699
    _globals["_DATABASESOURCETYPE"]._serialized_end = 9136
    _globals["_STREAMSOURCEREFERENCE"]._serialized_start = 108
    _globals["_STREAMSOURCEREFERENCE"]._serialized_end = 205
    _globals["_STREAMSOURCE"]._serialized_start = 208
    _globals["_STREAMSOURCE"]._serialized_end = 400
    _globals["_KINESISSOURCE"]._serialized_start = 403
    _globals["_KINESISSOURCE"]._serialized_end = 897
    _globals["_KAFKASOURCE"]._serialized_start = 900
    _globals["_KAFKASOURCE"]._serialized_end = 1458
    _globals["_PUBSUBSOURCE"]._serialized_start = 1461
    _globals["_PUBSUBSOURCE"]._serialized_end = 1701
    _globals["_DATABASESOURCEREFERENCE"]._serialized_start = 1703
    _globals["_DATABASESOURCEREFERENCE"]._serialized_end = 1804
    _globals["_DATABASESOURCE"]._serialized_start = 1807
    _globals["_DATABASESOURCE"]._serialized_end = 2497
    _globals["_BIGQUERYSOURCE"]._serialized_start = 2500
    _globals["_BIGQUERYSOURCE"]._serialized_end = 3073
    _globals["_BIGQUERYSOURCE_ENGINEARGSENTRY"]._serialized_start = 2886
    _globals["_BIGQUERYSOURCE_ENGINEARGSENTRY"]._serialized_end = 2976
    _globals["_BIGQUERYSOURCE_ASYNCENGINEARGSENTRY"]._serialized_start = 2978
    _globals["_BIGQUERYSOURCE_ASYNCENGINEARGSENTRY"]._serialized_end = 3073
    _globals["_CLOUDSQLSOURCE"]._serialized_start = 3076
    _globals["_CLOUDSQLSOURCE"]._serialized_end = 3580
    _globals["_CLOUDSQLSOURCE_ENGINEARGSENTRY"]._serialized_start = 2886
    _globals["_CLOUDSQLSOURCE_ENGINEARGSENTRY"]._serialized_end = 2976
    _globals["_CLOUDSQLSOURCE_ASYNCENGINEARGSENTRY"]._serialized_start = 2978
    _globals["_CLOUDSQLSOURCE_ASYNCENGINEARGSENTRY"]._serialized_end = 3073
    _globals["_DATABRICKSSOURCE"]._serialized_start = 3583
    _globals["_DATABRICKSSOURCE"]._serialized_end = 4112
    _globals["_DATABRICKSSOURCE_ENGINEARGSENTRY"]._serialized_start = 2886
    _globals["_DATABRICKSSOURCE_ENGINEARGSENTRY"]._serialized_end = 2976
    _globals["_DATABRICKSSOURCE_ASYNCENGINEARGSENTRY"]._serialized_start = 2978
    _globals["_DATABRICKSSOURCE_ASYNCENGINEARGSENTRY"]._serialized_end = 3073
    _globals["_DYNAMODBSOURCE"]._serialized_start = 4115
    _globals["_DYNAMODBSOURCE"]._serialized_end = 4849
    _globals["_DYNAMODBSOURCE_ENGINEARGSENTRY"]._serialized_start = 2886
    _globals["_DYNAMODBSOURCE_ENGINEARGSENTRY"]._serialized_end = 2976
    _globals["_DYNAMODBSOURCE_ASYNCENGINEARGSENTRY"]._serialized_start = 2978
    _globals["_DYNAMODBSOURCE_ASYNCENGINEARGSENTRY"]._serialized_end = 3073
    _globals["_MYSQLSOURCE"]._serialized_start = 4852
    _globals["_MYSQLSOURCE"]._serialized_end = 5350
    _globals["_MYSQLSOURCE_ENGINEARGSENTRY"]._serialized_start = 2886
    _globals["_MYSQLSOURCE_ENGINEARGSENTRY"]._serialized_end = 2976
    _globals["_MYSQLSOURCE_ASYNCENGINEARGSENTRY"]._serialized_start = 2978
    _globals["_MYSQLSOURCE_ASYNCENGINEARGSENTRY"]._serialized_end = 3073
    _globals["_POSTGRESSOURCE"]._serialized_start = 5353
    _globals["_POSTGRESSOURCE"]._serialized_end = 5860
    _globals["_POSTGRESSOURCE_ENGINEARGSENTRY"]._serialized_start = 2886
    _globals["_POSTGRESSOURCE_ENGINEARGSENTRY"]._serialized_end = 2976
    _globals["_POSTGRESSOURCE_ASYNCENGINEARGSENTRY"]._serialized_start = 2978
    _globals["_POSTGRESSOURCE_ASYNCENGINEARGSENTRY"]._serialized_end = 3073
    _globals["_REDSHIFTSOURCE"]._serialized_start = 5863
    _globals["_REDSHIFTSOURCE"]._serialized_end = 6428
    _globals["_REDSHIFTSOURCE_ENGINEARGSENTRY"]._serialized_start = 2886
    _globals["_REDSHIFTSOURCE_ENGINEARGSENTRY"]._serialized_end = 2976
    _globals["_REDSHIFTSOURCE_ASYNCENGINEARGSENTRY"]._serialized_start = 2978
    _globals["_REDSHIFTSOURCE_ASYNCENGINEARGSENTRY"]._serialized_end = 3073
    _globals["_SNOWFLAKESOURCE"]._serialized_start = 6431
    _globals["_SNOWFLAKESOURCE"]._serialized_end = 7062
    _globals["_SNOWFLAKESOURCE_ENGINEARGSENTRY"]._serialized_start = 2886
    _globals["_SNOWFLAKESOURCE_ENGINEARGSENTRY"]._serialized_end = 2976
    _globals["_SNOWFLAKESOURCE_ASYNCENGINEARGSENTRY"]._serialized_start = 2978
    _globals["_SNOWFLAKESOURCE_ASYNCENGINEARGSENTRY"]._serialized_end = 3073
    _globals["_SQLITESOURCE"]._serialized_start = 7065
    _globals["_SQLITESOURCE"]._serialized_end = 7491
    _globals["_SQLITESOURCE_ENGINEARGSENTRY"]._serialized_start = 2886
    _globals["_SQLITESOURCE_ENGINEARGSENTRY"]._serialized_end = 2976
    _globals["_SQLITESOURCE_ASYNCENGINEARGSENTRY"]._serialized_start = 2978
    _globals["_SQLITESOURCE_ASYNCENGINEARGSENTRY"]._serialized_end = 3073
    _globals["_SPANNERSOURCE"]._serialized_start = 7494
    _globals["_SPANNERSOURCE"]._serialized_end = 8011
    _globals["_SPANNERSOURCE_ENGINEARGSENTRY"]._serialized_start = 2886
    _globals["_SPANNERSOURCE_ENGINEARGSENTRY"]._serialized_end = 2976
    _globals["_SPANNERSOURCE_ASYNCENGINEARGSENTRY"]._serialized_start = 2978
    _globals["_SPANNERSOURCE_ASYNCENGINEARGSENTRY"]._serialized_end = 3073
    _globals["_TRINOSOURCE"]._serialized_start = 8014
    _globals["_TRINOSOURCE"]._serialized_end = 8546
    _globals["_TRINOSOURCE_ENGINEARGSENTRY"]._serialized_start = 2886
    _globals["_TRINOSOURCE_ENGINEARGSENTRY"]._serialized_end = 2976
    _globals["_TRINOSOURCE_ASYNCENGINEARGSENTRY"]._serialized_start = 2978
    _globals["_TRINOSOURCE_ASYNCENGINEARGSENTRY"]._serialized_end = 3073
# @@protoc_insertion_point(module_scope)
