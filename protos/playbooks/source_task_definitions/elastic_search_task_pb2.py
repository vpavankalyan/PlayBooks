# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/playbooks/source_task_definitions/elastic_search_task.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBprotos/playbooks/source_task_definitions/elastic_search_task.proto\x12\x10protos.playbooks\x1a\x1egoogle/protobuf/wrappers.proto\"\xa4\x02\n\rElasticSearch\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32(.protos.playbooks.ElasticSearch.TaskType\x12\x41\n\x0bquery_index\x18\x02 \x01(\x0b\x32*.protos.playbooks.ElasticSearch.QueryIndexH\x00\x1a\x66\n\nQueryIndex\x12+\n\x05index\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05query\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"(\n\x08TaskType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bQUERY_INDEX\x10\x01\x42\x06\n\x04taskb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.playbooks.source_task_definitions.elastic_search_task_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ELASTICSEARCH._serialized_start=121
  _ELASTICSEARCH._serialized_end=413
  _ELASTICSEARCH_QUERYINDEX._serialized_start=261
  _ELASTICSEARCH_QUERYINDEX._serialized_end=363
  _ELASTICSEARCH_TASKTYPE._serialized_start=365
  _ELASTICSEARCH_TASKTYPE._serialized_end=405
# @@protoc_insertion_point(module_scope)