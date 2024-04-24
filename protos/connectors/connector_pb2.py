# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/connectors/connector.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!protos/connectors/connector.proto\x12\x11protos.connectors\x1a\x1egoogle/protobuf/wrappers.proto\"T\n\x11PeriodicRunStatus\"?\n\nStatusType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\x0c\n\x08\x46INISHED\x10\x02\x12\t\n\x05\x45RROR\x10\x03\"\xcb\x03\n\tConnector\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12.\n\x04type\x18\x02 \x01(\x0e\x32 .protos.connectors.ConnectorType\x12-\n\tis_active\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x04name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\ncreated_by\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x12\n\ncreated_at\x18\x06 \x01(\x10\x12\x12\n\nupdated_at\x18\x07 \x01(\x10\x12\x32\n\x0c\x64isplay_name\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x63\x61tegory\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x41\n\rsentry_config\x18\n \x01(\x0b\x32(.protos.connectors.SentryConnectorConfigH\x00\x42\x08\n\x06\x63onfig\"P\n\x15SentryConnectorConfig\x12\x37\n\x11polling_frequency\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\"\x83\x0b\n\x0c\x43onnectorKey\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x39\n\x08key_type\x18\x02 \x01(\x0e\x32\'.protos.connectors.ConnectorKey.KeyType\x12)\n\x03key\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\tis_active\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0c\x63onnector_id\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x12\n\ncreated_at\x18\x06 \x01(\x10\x12\x12\n\nupdated_at\x18\x07 \x01(\x10\x12\x32\n\x0c\x64isplay_name\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xa3\x08\n\x07KeyType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x12\n\x0eSENTRY_API_KEY\x10\x01\x12\x13\n\x0fSENTRY_ORG_SLUG\x10\x06\x12\x13\n\x0f\x44\x41TADOG_APP_KEY\x10\x02\x12\x13\n\x0f\x44\x41TADOG_API_KEY\x10\x03\x12\x16\n\x12\x44\x41TADOG_AUTH_TOKEN\x10\x0f\x12\x16\n\x12\x44\x41TADOG_API_DOMAIN\x10\x12\x12\x14\n\x10NEWRELIC_API_KEY\x10\x04\x12\x13\n\x0fNEWRELIC_APP_ID\x10\x05\x12\x16\n\x12NEWRELIC_QUERY_KEY\x10\x07\x12\x17\n\x13NEWRELIC_API_DOMAIN\x10\x13\x12\x18\n\x14SLACK_BOT_AUTH_TOKEN\x10\x08\x12\x11\n\rSLACK_CHANNEL\x10\t\x12\x18\n\x14HONEYBADGER_USERNAME\x10\n\x12\x18\n\x14HONEYBADGER_PASSWORD\x10\x0b\x12\x1a\n\x16HONEYBADGER_PROJECT_ID\x10\x0c\x12\x12\n\x0e\x41WS_ACCESS_KEY\x10\r\x12\x12\n\x0e\x41WS_SECRET_KEY\x10\x0e\x12\x0e\n\nAWS_REGION\x10\x14\x12\x18\n\x14\x41WS_ASSUMED_ROLE_ARN\x10\x17\x12\x10\n\x0c\x45KS_ROLE_ARN\x10(\x12\x1f\n\x1bGOOGLE_CHAT_BOT_OAUTH_TOKEN\x10\x10\x12\x1a\n\x16GOOGLE_CHAT_BOT_SPACES\x10\x11\x12\x10\n\x0cGRAFANA_HOST\x10\x15\x12\x13\n\x0fGRAFANA_API_KEY\x10\x16\x12\x18\n\x14\x43LICKHOUSE_INTERFACE\x10\x18\x12\x13\n\x0f\x43LICKHOUSE_HOST\x10\x19\x12\x13\n\x0f\x43LICKHOUSE_PORT\x10\x1a\x12\x13\n\x0f\x43LICKHOUSE_USER\x10\x1b\x12\x17\n\x13\x43LICKHOUSE_PASSWORD\x10\x1c\x12\x12\n\x0eGCM_PROJECT_ID\x10\x1d\x12\x13\n\x0fGCM_PRIVATE_KEY\x10\x1e\x12\x14\n\x10GCM_CLIENT_EMAIL\x10\x1f\x12\x11\n\rGCM_TOKEN_URI\x10 \x12\x11\n\rPOSTGRES_HOST\x10!\x12\x11\n\rPOSTGRES_USER\x10\"\x12\x15\n\x11POSTGRES_PASSWORD\x10#\x12\x11\n\rPOSTGRES_PORT\x10$\x12\x15\n\x11POSTGRES_DATABASE\x10%\x12\x14\n\x10POSTGRES_OPTIONS\x10&\x12\x1c\n\x18\x44\x42_CONNECTION_STRING_URI\x10\'\x12\x16\n\x12PAGER_DUTY_API_KEY\x10)\x12\x15\n\x11OPS_GENIE_API_KEY\x10*\x12\x14\n\x10\x41GENT_PROXY_HOST\x10+\x12\x17\n\x13\x41GENT_PROXY_API_KEY\x10,\x12\x18\n\x14GITHUB_ACTIONS_TOKEN\x10-\x12\x10\n\x0cSLACK_APP_ID\x10.\"\xa8\x05\n\x11UpdateConnectorOp\x12\x33\n\x02op\x18\x01 \x01(\x0e\x32\'.protos.connectors.UpdateConnectorOp.Op\x12Y\n\x15update_connector_name\x18\x02 \x01(\x0b\x32\x38.protos.connectors.UpdateConnectorOp.UpdateConnectorNameH\x00\x12]\n\x17update_connector_status\x18\x03 \x01(\x0b\x32:.protos.connectors.UpdateConnectorOp.UpdateConnectorStatusH\x00\x12Y\n\x15update_connector_keys\x18\x04 \x01(\x0b\x32\x38.protos.connectors.UpdateConnectorOp.UpdateConnectorKeysH\x00\x1a\x41\n\x13UpdateConnectorName\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x1a\x46\n\x15UpdateConnectorStatus\x12-\n\tis_active\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x1aN\n\x13UpdateConnectorKeys\x12\x37\n\x0e\x63onnector_keys\x18\x01 \x03(\x0b\x32\x1f.protos.connectors.ConnectorKey\"d\n\x02Op\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x19\n\x15UPDATE_CONNECTOR_NAME\x10\x01\x12\x1b\n\x17UPDATE_CONNECTOR_STATUS\x10\x02\x12\x19\n\x15UPDATE_CONNECTOR_KEYS\x10\x03\x42\x08\n\x06update\"\xe1\x02\n AccountActiveConnectorModelTypes\x12\x38\n\x0e\x63onnector_type\x18\x01 \x01(\x0e\x32 .protos.connectors.ConnectorType\x12j\n\x0fmodel_types_map\x18\x02 \x03(\x0b\x32Q.protos.connectors.AccountActiveConnectorModelTypes.ConnectorMetadataModelTypeMap\x1a\x96\x01\n\x1d\x43onnectorMetadataModelTypeMap\x12\x41\n\nmodel_type\x18\x01 \x01(\x0e\x32-.protos.connectors.ConnectorMetadataModelType\x12\x32\n\x0c\x64isplay_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue*\xc0\x04\n\rConnectorType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06SENTRY\x10\x01\x12\x0b\n\x07SEGMENT\x10\x02\x12\x12\n\x0e\x45LASTIC_SEARCH\x10\x03\x12\r\n\tAMPLITUDE\x10\x04\x12\x0f\n\x0b\x41WS_KINESIS\x10\x05\x12\x0e\n\nCLOUDWATCH\x10\x06\x12\r\n\tCLEVERTAP\x10\x07\x12\x0f\n\x0bRUDDERSTACK\x10\x08\x12\x0c\n\x08MOENGAGE\x10\t\x12\t\n\x05\x43RIBL\x10\n\x12\t\n\x05KAFKA\x10\x0b\x12\x0b\n\x07\x44\x41TADOG\x10\x0c\x12\x0c\n\x08\x46ILEBEAT\x10\r\x12\x0c\n\x08LOGSTASH\x10\x0e\x12\x0b\n\x07\x46LUENTD\x10\x0f\x12\r\n\tFLUENTBIT\x10\x10\x12\x0e\n\nPAGER_DUTY\x10\x11\x12\r\n\tNEW_RELIC\x10\x12\x12\t\n\x05SLACK\x10\x13\x12\x0f\n\x0bHONEYBADGER\x10\x14\x12\x0f\n\x0bGOOGLE_CHAT\x10\x15\x12\x11\n\rDATADOG_OAUTH\x10\x16\x12\x07\n\x03GCM\x10\x17\x12\x0e\n\nPROMETHEUS\x10\x18\x12\x0f\n\x0b\x45LASTIC_APM\x10\x19\x12\x14\n\x10VICTORIA_METRICS\x10\x1a\x12\x11\n\rSLACK_CONNECT\x10\x1b\x12\x0b\n\x07GRAFANA\x10\x1c\x12\x0e\n\nCLICKHOUSE\x10\x1d\x12\x11\n\rDOCUMENTATION\x10\x1e\x12\x0c\n\x08POSTGRES\x10\x1f\x12\r\n\tOPS_GENIE\x10 \x12\x07\n\x03\x45KS\x10!\x12\x0f\n\x0b\x41GENT_PROXY\x10\"\x12\x0f\n\x0bGRAFANA_VPC\x10#\x12\x12\n\x0eGITHUB_ACTIONS\x10$*\x8e\x06\n\x1a\x43onnectorMetadataModelType\x12\x0e\n\nUNKNOWN_MT\x10\x00\x12\x14\n\x10NEW_RELIC_POLICY\x10\x01\x12\x17\n\x13NEW_RELIC_CONDITION\x10\x02\x12\x14\n\x10NEW_RELIC_ENTITY\x10\x03\x12\x1e\n\x1aNEW_RELIC_ENTITY_DASHBOARD\x10\x04\x12 \n\x1cNEW_RELIC_ENTITY_APPLICATION\x10\x05\x12\x12\n\x0eNEW_RELIC_NRQL\x10\x06\x12\x13\n\x0f\x44\x41TADOG_MONITOR\x10\x65\x12\x15\n\x11\x44\x41TADOG_DASHBOARD\x10\x66\x12 \n\x1c\x44\x41TADOG_LIVE_INTEGRATION_AWS\x10g\x12$\n DATADOG_LIVE_INTEGRATION_AWS_LOG\x10h\x12\"\n\x1e\x44\x41TADOG_LIVE_INTEGRATION_AZURE\x10i\x12\'\n#DATADOG_LIVE_INTEGRATION_CLOUDFLARE\x10j\x12#\n\x1f\x44\x41TADOG_LIVE_INTEGRATION_FASTLY\x10k\x12 \n\x1c\x44\x41TADOG_LIVE_INTEGRATION_GCP\x10l\x12&\n\"DATADOG_LIVE_INTEGRATION_CONFLUENT\x10m\x12\x13\n\x0f\x44\x41TADOG_SERVICE\x10n\x12\x12\n\x0e\x44\x41TADOG_METRIC\x10o\x12\x16\n\x11\x43LOUDWATCH_METRIC\x10\xc9\x01\x12\x19\n\x14\x43LOUDWATCH_LOG_GROUP\x10\xca\x01\x12\x17\n\x12GRAFANA_DATASOURCE\x10\xad\x02\x12\x16\n\x11GRAFANA_DASHBOARD\x10\xae\x02\x12!\n\x1cGRAFANA_TARGET_METRIC_PROMQL\x10\xaf\x02\x12\x18\n\x13\x43LICKHOUSE_DATABASE\x10\x91\x03\x12\x12\n\rSLACK_CHANNEL\x10\xf5\x03\x12\r\n\x08MARKDOWN\x10\xd9\x04\x12\x16\n\x11POSTGRES_DATABASE\x10\xbd\x05\x12\x10\n\x0b\x45KS_CLUSTER\x10\xa1\x06*\xb2\x01\n\x0fTransformerType\x12\x0e\n\nUNKNOWN_TT\x10\x00\x12\x1e\n\x1aSEGMENT_DFAULT_TRANSFORMER\x10\x02\x12!\n\x1d\x41MPLITUDE_DEFAULT_TRANSFORMER\x10\x03\x12\'\n#PRODIGAL_CLOUDWATCH_LOG_TRANSFORMER\x10\x04\x12#\n\x1f\x43LOUDWATCH_JSON_LOG_TRANSFORMER\x10\x05*Z\n\x0b\x44\x65\x63oderType\x12\x0e\n\nUNKNOWN_DT\x10\x00\x12\x17\n\x13\x41WS_KINESIS_DECODER\x10\x01\x12\"\n\x1e\x41WS_CLOUDWATCH_KINESIS_DECODER\x10\x02*4\n\nReportType\x12\x0e\n\nUNKNOWN_RT\x10\x00\x12\x0b\n\x07INITIAL\x10\x01\x12\t\n\x05\x46INAL\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.connectors.connector_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONNECTORTYPE._serialized_start=3172
  _CONNECTORTYPE._serialized_end=3748
  _CONNECTORMETADATAMODELTYPE._serialized_start=3751
  _CONNECTORMETADATAMODELTYPE._serialized_end=4533
  _TRANSFORMERTYPE._serialized_start=4536
  _TRANSFORMERTYPE._serialized_end=4714
  _DECODERTYPE._serialized_start=4716
  _DECODERTYPE._serialized_end=4806
  _REPORTTYPE._serialized_start=4808
  _REPORTTYPE._serialized_end=4860
  _PERIODICRUNSTATUS._serialized_start=88
  _PERIODICRUNSTATUS._serialized_end=172
  _PERIODICRUNSTATUS_STATUSTYPE._serialized_start=109
  _PERIODICRUNSTATUS_STATUSTYPE._serialized_end=172
  _CONNECTOR._serialized_start=175
  _CONNECTOR._serialized_end=634
  _SENTRYCONNECTORCONFIG._serialized_start=636
  _SENTRYCONNECTORCONFIG._serialized_end=716
  _CONNECTORKEY._serialized_start=719
  _CONNECTORKEY._serialized_end=2130
  _CONNECTORKEY_KEYTYPE._serialized_start=1071
  _CONNECTORKEY_KEYTYPE._serialized_end=2130
  _UPDATECONNECTOROP._serialized_start=2133
  _UPDATECONNECTOROP._serialized_end=2813
  _UPDATECONNECTOROP_UPDATECONNECTORNAME._serialized_start=2484
  _UPDATECONNECTOROP_UPDATECONNECTORNAME._serialized_end=2549
  _UPDATECONNECTOROP_UPDATECONNECTORSTATUS._serialized_start=2551
  _UPDATECONNECTOROP_UPDATECONNECTORSTATUS._serialized_end=2621
  _UPDATECONNECTOROP_UPDATECONNECTORKEYS._serialized_start=2623
  _UPDATECONNECTOROP_UPDATECONNECTORKEYS._serialized_end=2701
  _UPDATECONNECTOROP_OP._serialized_start=2703
  _UPDATECONNECTOROP_OP._serialized_end=2803
  _ACCOUNTACTIVECONNECTORMODELTYPES._serialized_start=2816
  _ACCOUNTACTIVECONNECTORMODELTYPES._serialized_end=3169
  _ACCOUNTACTIVECONNECTORMODELTYPES_CONNECTORMETADATAMODELTYPEMAP._serialized_start=3019
  _ACCOUNTACTIVECONNECTORMODELTYPES_CONNECTORMETADATAMODELTYPEMAP._serialized_end=3169
# @@protoc_insertion_point(module_scope)
