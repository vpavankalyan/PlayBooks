# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/playbooks/source_task_definitions/azure_task.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9protos/playbooks/source_task_definitions/azure_task.proto\x12\x10protos.playbooks\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xe1\x02\n\x05\x41zure\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .protos.playbooks.Azure.TaskType\x12\x44\n\x11\x66ilter_log_events\x18\x02 \x01(\x0b\x32\'.protos.playbooks.Azure.FilterLogEventsH\x00\x1a\xa9\x01\n\x0f\x46ilterLogEvents\x12\x32\n\x0cworkspace_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0c\x66ilter_query\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08timespan\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\".\n\x08TaskType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x15\n\x11\x46ILTER_LOG_EVENTS\x10\x01\x42\x06\n\x04taskb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.playbooks.source_task_definitions.azure_task_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AZURE._serialized_start=142
  _AZURE._serialized_end=495
  _AZURE_FILTERLOGEVENTS._serialized_start=270
  _AZURE_FILTERLOGEVENTS._serialized_end=439
  _AZURE_TASKTYPE._serialized_start=441
  _AZURE_TASKTYPE._serialized_end=487
# @@protoc_insertion_point(module_scope)