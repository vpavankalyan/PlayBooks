# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/playbooks/source_task_definitions/gcm_task.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7protos/playbooks/source_task_definitions/gcm_task.proto\x12\x10protos.playbooks\x1a\x1egoogle/protobuf/wrappers.proto\"\xdb\x03\n\x03Gcm\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.protos.playbooks.Gcm.TaskType\x12\x34\n\x0bget_metrics\x18\x02 \x01(\x0b\x32\x1d.protos.playbooks.Gcm.CommandH\x00\x12\x31\n\x08get_logs\x18\x03 \x01(\x0b\x32\x1d.protos.playbooks.Gcm.CommandH\x00\x1a\xfc\x01\n\x07\x43ommand\x12\x31\n\x0b\x64\x65scription\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nmetricType\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\tstartTime\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07\x65ndTime\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06\x66ilter\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"6\n\x08TaskType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bGET_METRICS\x10\x01\x12\x0c\n\x08GET_LOGS\x10\x02\x42\x06\n\x04taskb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.playbooks.source_task_definitions.gcm_task_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GCM._serialized_start=110
  _GCM._serialized_end=585
  _GCM_COMMAND._serialized_start=269
  _GCM_COMMAND._serialized_end=521
  _GCM_TASKTYPE._serialized_start=523
  _GCM_TASKTYPE._serialized_end=577
# @@protoc_insertion_point(module_scope)