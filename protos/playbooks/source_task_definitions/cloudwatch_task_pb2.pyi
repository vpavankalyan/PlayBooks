"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CloudwatchMetricExecutionTask(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Dimension(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        @property
        def name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def value(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        def __init__(
            self,
            *,
            name: google.protobuf.wrappers_pb2.StringValue | None = ...,
            value: google.protobuf.wrappers_pb2.StringValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["name", b"name", "value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "value", b"value"]) -> None: ...

    NAMESPACE_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    METRIC_NAME_FIELD_NUMBER: builtins.int
    DIMENSIONS_FIELD_NUMBER: builtins.int
    STATISTIC_FIELD_NUMBER: builtins.int
    PROCESS_FUNCTION_FIELD_NUMBER: builtins.int
    @property
    def namespace(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def region(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def metric_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def dimensions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CloudwatchMetricExecutionTask.Dimension]: ...
    @property
    def statistic(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def process_function(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        namespace: google.protobuf.wrappers_pb2.StringValue | None = ...,
        region: google.protobuf.wrappers_pb2.StringValue | None = ...,
        metric_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        dimensions: collections.abc.Iterable[global___CloudwatchMetricExecutionTask.Dimension] | None = ...,
        statistic: google.protobuf.wrappers_pb2.StringValue | None = ...,
        process_function: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["metric_name", b"metric_name", "namespace", b"namespace", "process_function", b"process_function", "region", b"region", "statistic", b"statistic"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dimensions", b"dimensions", "metric_name", b"metric_name", "namespace", b"namespace", "process_function", b"process_function", "region", b"region", "statistic", b"statistic"]) -> None: ...

global___CloudwatchMetricExecutionTask = CloudwatchMetricExecutionTask

@typing_extensions.final
class CloudwatchFilterLogEventsTask(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGION_FIELD_NUMBER: builtins.int
    LOG_GROUP_NAME_FIELD_NUMBER: builtins.int
    FILTER_QUERY_FIELD_NUMBER: builtins.int
    @property
    def region(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def log_group_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def filter_query(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        region: google.protobuf.wrappers_pb2.StringValue | None = ...,
        log_group_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        filter_query: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter_query", b"filter_query", "log_group_name", b"log_group_name", "region", b"region"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter_query", b"filter_query", "log_group_name", b"log_group_name", "region", b"region"]) -> None: ...

global___CloudwatchFilterLogEventsTask = CloudwatchFilterLogEventsTask

@typing_extensions.final
class PlaybookCloudwatchTask(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _TaskType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TaskTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PlaybookCloudwatchTask._TaskType.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: PlaybookCloudwatchTask._TaskType.ValueType  # 0
        METRIC_EXECUTION: PlaybookCloudwatchTask._TaskType.ValueType  # 1
        FILTER_LOG_EVENTS: PlaybookCloudwatchTask._TaskType.ValueType  # 2

    class TaskType(_TaskType, metaclass=_TaskTypeEnumTypeWrapper): ...
    UNKNOWN: PlaybookCloudwatchTask.TaskType.ValueType  # 0
    METRIC_EXECUTION: PlaybookCloudwatchTask.TaskType.ValueType  # 1
    FILTER_LOG_EVENTS: PlaybookCloudwatchTask.TaskType.ValueType  # 2

    TYPE_FIELD_NUMBER: builtins.int
    METRIC_EXECUTION_TASK_FIELD_NUMBER: builtins.int
    FILTER_LOG_EVENTS_TASK_FIELD_NUMBER: builtins.int
    type: global___PlaybookCloudwatchTask.TaskType.ValueType
    @property
    def metric_execution_task(self) -> global___CloudwatchMetricExecutionTask: ...
    @property
    def filter_log_events_task(self) -> global___CloudwatchFilterLogEventsTask: ...
    def __init__(
        self,
        *,
        type: global___PlaybookCloudwatchTask.TaskType.ValueType = ...,
        metric_execution_task: global___CloudwatchMetricExecutionTask | None = ...,
        filter_log_events_task: global___CloudwatchFilterLogEventsTask | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter_log_events_task", b"filter_log_events_task", "metric_execution_task", b"metric_execution_task", "task", b"task"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter_log_events_task", b"filter_log_events_task", "metric_execution_task", b"metric_execution_task", "task", b"task", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["task", b"task"]) -> typing_extensions.Literal["metric_execution_task", "filter_log_events_task"] | None: ...

global___PlaybookCloudwatchTask = PlaybookCloudwatchTask