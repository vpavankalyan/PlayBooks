# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/playbooks/source_task_definitions/promql_task.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import base_pb2 as protos_dot_base__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:protos/playbooks/source_task_definitions/promql_task.proto\x12\x10protos.playbooks\x1a\x11protos/base.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x86\x03\n\x12PlaybookPromQLTask\x12;\n\x04type\x18\x01 \x01(\x0e\x32-.protos.playbooks.PlaybookPromQLTask.TaskType\x12\x66\n\x1cpromql_metric_execution_task\x18\x03 \x01(\x0b\x32>.protos.playbooks.PlaybookPromQLTask.PromQlMetricExecutionTaskH\x00\x1a\x8c\x01\n\x19PromQlMetricExecutionTask\x12\x37\n\x11promql_expression\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10process_function\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"4\n\x08TaskType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x1b\n\x17PROMQL_METRIC_EXECUTION\x10\x01\x42\x06\n\x04taskb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.playbooks.source_task_definitions.promql_task_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYBOOKPROMQLTASK._serialized_start=132
  _PLAYBOOKPROMQLTASK._serialized_end=522
  _PLAYBOOKPROMQLTASK_PROMQLMETRICEXECUTIONTASK._serialized_start=320
  _PLAYBOOKPROMQLTASK_PROMQLMETRICEXECUTIONTASK._serialized_end=460
  _PLAYBOOKPROMQLTASK_TASKTYPE._serialized_start=462
  _PLAYBOOKPROMQLTASK_TASKTYPE._serialized_end=514
# @@protoc_insertion_point(module_scope)