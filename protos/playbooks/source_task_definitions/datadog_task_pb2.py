# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/playbooks/source_task_definitions/datadog_task.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import base_pb2 as protos_dot_base__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;protos/playbooks/source_task_definitions/datadog_task.proto\x12\x10protos.playbooks\x1a\x11protos/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xa3\x02\n\x1aServiceMetricExecutionTask\x12\x32\n\x0cservice_name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10\x65nvironment_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rmetric_family\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06metric\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10process_function\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x92\x01\n\x18QueryMetricExecutionTask\x12\x0f\n\x07queries\x18\x01 \x03(\t\x12-\n\x07\x66ormula\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10process_function\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xd8\x02\n\x13PlaybookDatadogTask\x12<\n\x04type\x18\x01 \x01(\x0e\x32..protos.playbooks.PlaybookDatadogTask.TaskType\x12U\n\x1dservice_metric_execution_task\x18\x02 \x01(\x0b\x32,.protos.playbooks.ServiceMetricExecutionTaskH\x00\x12Q\n\x1bquery_metric_execution_task\x18\x03 \x01(\x0b\x32*.protos.playbooks.QueryMetricExecutionTaskH\x00\"Q\n\x08TaskType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x1c\n\x18SERVICE_METRIC_EXECUTION\x10\x01\x12\x1a\n\x16QUERY_METRIC_EXECUTION\x10\x02\x42\x06\n\x04taskb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.playbooks.source_task_definitions.datadog_task_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SERVICEMETRICEXECUTIONTASK._serialized_start=133
  _SERVICEMETRICEXECUTIONTASK._serialized_end=424
  _QUERYMETRICEXECUTIONTASK._serialized_start=427
  _QUERYMETRICEXECUTIONTASK._serialized_end=573
  _PLAYBOOKDATADOGTASK._serialized_start=576
  _PLAYBOOKDATADOGTASK._serialized_end=920
  _PLAYBOOKDATADOGTASK_TASKTYPE._serialized_start=831
  _PLAYBOOKDATADOGTASK_TASKTYPE._serialized_end=912
# @@protoc_insertion_point(module_scope)
