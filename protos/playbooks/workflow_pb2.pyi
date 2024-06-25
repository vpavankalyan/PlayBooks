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
import google.protobuf.struct_pb2
import google.protobuf.wrappers_pb2
import protos.base_pb2
import protos.playbooks.playbook_pb2
import protos.playbooks.workflow_actions.api_trigger_pb2
import protos.playbooks.workflow_actions.ms_teams_message_webhook_pb2
import protos.playbooks.workflow_actions.pd_notes_pb2
import protos.playbooks.workflow_actions.slack_message_pb2
import protos.playbooks.workflow_actions.slack_thread_reply_pb2
import protos.playbooks.workflow_entry_points.api_entry_point_pb2
import protos.playbooks.workflow_entry_points.pd_incident_entry_point_pb2
import protos.playbooks.workflow_entry_points.slack_alert_entry_point_pb2
import protos.playbooks.workflow_schedules.cron_schedule_pb2
import protos.playbooks.workflow_schedules.interval_schedule_pb2
import protos.playbooks.workflow_schedules.one_off_schedule_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _WorkflowExecutionStatusType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _WorkflowExecutionStatusTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_WorkflowExecutionStatusType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN_WORKFLOW_STATUS: _WorkflowExecutionStatusType.ValueType  # 0
    WORKFLOW_SCHEDULED: _WorkflowExecutionStatusType.ValueType  # 1
    WORKFLOW_RUNNING: _WorkflowExecutionStatusType.ValueType  # 2
    WORKFLOW_FINISHED: _WorkflowExecutionStatusType.ValueType  # 3
    WORKFLOW_FAILED: _WorkflowExecutionStatusType.ValueType  # 4
    WORKFLOW_CANCELLED: _WorkflowExecutionStatusType.ValueType  # 5

class WorkflowExecutionStatusType(_WorkflowExecutionStatusType, metaclass=_WorkflowExecutionStatusTypeEnumTypeWrapper): ...

UNKNOWN_WORKFLOW_STATUS: WorkflowExecutionStatusType.ValueType  # 0
WORKFLOW_SCHEDULED: WorkflowExecutionStatusType.ValueType  # 1
WORKFLOW_RUNNING: WorkflowExecutionStatusType.ValueType  # 2
WORKFLOW_FINISHED: WorkflowExecutionStatusType.ValueType  # 3
WORKFLOW_FAILED: WorkflowExecutionStatusType.ValueType  # 4
WORKFLOW_CANCELLED: WorkflowExecutionStatusType.ValueType  # 5
global___WorkflowExecutionStatusType = WorkflowExecutionStatusType

@typing_extensions.final
class WorkflowConfiguration(google.protobuf.message.Message):
    """/////////////////// Workflow Configurations /////////////////////"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GENERATE_SUMMARY_FIELD_NUMBER: builtins.int
    GLOBAL_VARIABLE_SET_FIELD_NUMBER: builtins.int
    @property
    def generate_summary(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def global_variable_set(self) -> google.protobuf.struct_pb2.Struct: ...
    def __init__(
        self,
        *,
        generate_summary: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        global_variable_set: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["generate_summary", b"generate_summary", "global_variable_set", b"global_variable_set"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["generate_summary", b"generate_summary", "global_variable_set", b"global_variable_set"]) -> None: ...

global___WorkflowConfiguration = WorkflowConfiguration

@typing_extensions.final
class WorkflowSchedule(google.protobuf.message.Message):
    """/////////////////// Workflow Schedules /////////////////////"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[WorkflowSchedule._Type.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: WorkflowSchedule._Type.ValueType  # 0
        ONE_OFF: WorkflowSchedule._Type.ValueType  # 1
        INTERVAL: WorkflowSchedule._Type.ValueType  # 2
        CRON: WorkflowSchedule._Type.ValueType  # 3

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    UNKNOWN: WorkflowSchedule.Type.ValueType  # 0
    ONE_OFF: WorkflowSchedule.Type.ValueType  # 1
    INTERVAL: WorkflowSchedule.Type.ValueType  # 2
    CRON: WorkflowSchedule.Type.ValueType  # 3

    TYPE_FIELD_NUMBER: builtins.int
    ONE_OFF_FIELD_NUMBER: builtins.int
    INTERVAL_FIELD_NUMBER: builtins.int
    CRON_FIELD_NUMBER: builtins.int
    type: global___WorkflowSchedule.Type.ValueType
    @property
    def one_off(self) -> protos.playbooks.workflow_schedules.one_off_schedule_pb2.OneOffSchedule: ...
    @property
    def interval(self) -> protos.playbooks.workflow_schedules.interval_schedule_pb2.IntervalSchedule: ...
    @property
    def cron(self) -> protos.playbooks.workflow_schedules.cron_schedule_pb2.CronSchedule: ...
    def __init__(
        self,
        *,
        type: global___WorkflowSchedule.Type.ValueType = ...,
        one_off: protos.playbooks.workflow_schedules.one_off_schedule_pb2.OneOffSchedule | None = ...,
        interval: protos.playbooks.workflow_schedules.interval_schedule_pb2.IntervalSchedule | None = ...,
        cron: protos.playbooks.workflow_schedules.cron_schedule_pb2.CronSchedule | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cron", b"cron", "interval", b"interval", "one_off", b"one_off", "scheduler", b"scheduler"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cron", b"cron", "interval", b"interval", "one_off", b"one_off", "scheduler", b"scheduler", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["scheduler", b"scheduler"]) -> typing_extensions.Literal["one_off", "interval", "cron"] | None: ...

global___WorkflowSchedule = WorkflowSchedule

@typing_extensions.final
class WorkflowEntryPoint(google.protobuf.message.Message):
    """/////////////////// Workflow Entry Points /////////////////////"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[WorkflowEntryPoint._Type.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: WorkflowEntryPoint._Type.ValueType  # 0
        API: WorkflowEntryPoint._Type.ValueType  # 1
        SLACK_CHANNEL_ALERT: WorkflowEntryPoint._Type.ValueType  # 2
        PAGERDUTY_INCIDENT: WorkflowEntryPoint._Type.ValueType  # 3

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    UNKNOWN: WorkflowEntryPoint.Type.ValueType  # 0
    API: WorkflowEntryPoint.Type.ValueType  # 1
    SLACK_CHANNEL_ALERT: WorkflowEntryPoint.Type.ValueType  # 2
    PAGERDUTY_INCIDENT: WorkflowEntryPoint.Type.ValueType  # 3

    ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    API_FIELD_NUMBER: builtins.int
    SLACK_CHANNEL_ALERT_FIELD_NUMBER: builtins.int
    PAGERDUTY_INCIDENT_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    type: global___WorkflowEntryPoint.Type.ValueType
    @property
    def api(self) -> protos.playbooks.workflow_entry_points.api_entry_point_pb2.ApiWorkflowEntryPoint: ...
    @property
    def slack_channel_alert(self) -> protos.playbooks.workflow_entry_points.slack_alert_entry_point_pb2.SlackChannelAlertEntryPoint: ...
    @property
    def pagerduty_incident(self) -> protos.playbooks.workflow_entry_points.pd_incident_entry_point_pb2.PagerDutyIncidentEntryPoint: ...
    def __init__(
        self,
        *,
        id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        type: global___WorkflowEntryPoint.Type.ValueType = ...,
        api: protos.playbooks.workflow_entry_points.api_entry_point_pb2.ApiWorkflowEntryPoint | None = ...,
        slack_channel_alert: protos.playbooks.workflow_entry_points.slack_alert_entry_point_pb2.SlackChannelAlertEntryPoint | None = ...,
        pagerduty_incident: protos.playbooks.workflow_entry_points.pd_incident_entry_point_pb2.PagerDutyIncidentEntryPoint | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["api", b"api", "config", b"config", "id", b"id", "pagerduty_incident", b"pagerduty_incident", "slack_channel_alert", b"slack_channel_alert"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["api", b"api", "config", b"config", "id", b"id", "pagerduty_incident", b"pagerduty_incident", "slack_channel_alert", b"slack_channel_alert", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["config", b"config"]) -> typing_extensions.Literal["api", "slack_channel_alert", "pagerduty_incident"] | None: ...

global___WorkflowEntryPoint = WorkflowEntryPoint

@typing_extensions.final
class WorkflowAction(google.protobuf.message.Message):
    """/////////////////// Workflow Actions /////////////////////"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[WorkflowAction._Type.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: WorkflowAction._Type.ValueType  # 0
        API: WorkflowAction._Type.ValueType  # 1
        SLACK_MESSAGE: WorkflowAction._Type.ValueType  # 2
        SLACK_THREAD_REPLY: WorkflowAction._Type.ValueType  # 3
        MS_TEAMS_MESSAGE_WEBHOOK: WorkflowAction._Type.ValueType  # 4
        PAGERDUTY_NOTES: WorkflowAction._Type.ValueType  # 5

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    UNKNOWN: WorkflowAction.Type.ValueType  # 0
    API: WorkflowAction.Type.ValueType  # 1
    SLACK_MESSAGE: WorkflowAction.Type.ValueType  # 2
    SLACK_THREAD_REPLY: WorkflowAction.Type.ValueType  # 3
    MS_TEAMS_MESSAGE_WEBHOOK: WorkflowAction.Type.ValueType  # 4
    PAGERDUTY_NOTES: WorkflowAction.Type.ValueType  # 5

    @typing_extensions.final
    class WorkflowActionConnectorSource(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ID_FIELD_NUMBER: builtins.int
        SOURCE_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        @property
        def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
        source: protos.base_pb2.Source.ValueType
        @property
        def name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        def __init__(
            self,
            *,
            id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
            source: protos.base_pb2.Source.ValueType = ...,
            name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["id", b"id", "name", b"name"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "name", b"name", "source", b"source"]) -> None: ...

    TYPE_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    ACTION_CONNECTOR_SOURCE_FIELD_NUMBER: builtins.int
    API_FIELD_NUMBER: builtins.int
    SLACK_MESSAGE_FIELD_NUMBER: builtins.int
    SLACK_THREAD_REPLY_FIELD_NUMBER: builtins.int
    MS_TEAMS_MESSAGE_WEBHOOK_FIELD_NUMBER: builtins.int
    PAGERDUTY_NOTES_FIELD_NUMBER: builtins.int
    type: global___WorkflowAction.Type.ValueType
    source: protos.base_pb2.Source.ValueType
    @property
    def action_connector_source(self) -> global___WorkflowAction.WorkflowActionConnectorSource: ...
    @property
    def api(self) -> protos.playbooks.workflow_actions.api_trigger_pb2.ApiTriggerWorkflowAction: ...
    @property
    def slack_message(self) -> protos.playbooks.workflow_actions.slack_message_pb2.SlackMessageWorkflowAction: ...
    @property
    def slack_thread_reply(self) -> protos.playbooks.workflow_actions.slack_thread_reply_pb2.SlackThreadReplyWorkflowAction: ...
    @property
    def ms_teams_message_webhook(self) -> protos.playbooks.workflow_actions.ms_teams_message_webhook_pb2.MSTeamsMessageWebhookWorkflowAction: ...
    @property
    def pagerduty_notes(self) -> protos.playbooks.workflow_actions.pd_notes_pb2.PagerdutyNotesWorkflowAction: ...
    def __init__(
        self,
        *,
        type: global___WorkflowAction.Type.ValueType = ...,
        source: protos.base_pb2.Source.ValueType = ...,
        action_connector_source: global___WorkflowAction.WorkflowActionConnectorSource | None = ...,
        api: protos.playbooks.workflow_actions.api_trigger_pb2.ApiTriggerWorkflowAction | None = ...,
        slack_message: protos.playbooks.workflow_actions.slack_message_pb2.SlackMessageWorkflowAction | None = ...,
        slack_thread_reply: protos.playbooks.workflow_actions.slack_thread_reply_pb2.SlackThreadReplyWorkflowAction | None = ...,
        ms_teams_message_webhook: protos.playbooks.workflow_actions.ms_teams_message_webhook_pb2.MSTeamsMessageWebhookWorkflowAction | None = ...,
        pagerduty_notes: protos.playbooks.workflow_actions.pd_notes_pb2.PagerdutyNotesWorkflowAction | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["action_connector_source", b"action_connector_source", "api", b"api", "ms_teams_message_webhook", b"ms_teams_message_webhook", "notification_config", b"notification_config", "pagerduty_notes", b"pagerduty_notes", "slack_message", b"slack_message", "slack_thread_reply", b"slack_thread_reply"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["action_connector_source", b"action_connector_source", "api", b"api", "ms_teams_message_webhook", b"ms_teams_message_webhook", "notification_config", b"notification_config", "pagerduty_notes", b"pagerduty_notes", "slack_message", b"slack_message", "slack_thread_reply", b"slack_thread_reply", "source", b"source", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["notification_config", b"notification_config"]) -> typing_extensions.Literal["api", "slack_message", "slack_thread_reply", "ms_teams_message_webhook", "pagerduty_notes"] | None: ...

global___WorkflowAction = WorkflowAction

@typing_extensions.final
class Workflow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    SCHEDULE_FIELD_NUMBER: builtins.int
    PLAYBOOKS_FIELD_NUMBER: builtins.int
    ENTRY_POINTS_FIELD_NUMBER: builtins.int
    ACTIONS_FIELD_NUMBER: builtins.int
    LAST_EXECUTION_TIME_FIELD_NUMBER: builtins.int
    LAST_EXECUTION_STATUS_FIELD_NUMBER: builtins.int
    CONFIGURATION_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    @property
    def name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def description(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def created_by(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    created_at: builtins.int
    @property
    def is_active(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def schedule(self) -> global___WorkflowSchedule: ...
    @property
    def playbooks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[protos.playbooks.playbook_pb2.Playbook]: ...
    @property
    def entry_points(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WorkflowEntryPoint]: ...
    @property
    def actions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WorkflowAction]: ...
    last_execution_time: builtins.int
    last_execution_status: global___WorkflowExecutionStatusType.ValueType
    @property
    def configuration(self) -> global___WorkflowConfiguration: ...
    def __init__(
        self,
        *,
        id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        description: google.protobuf.wrappers_pb2.StringValue | None = ...,
        created_by: google.protobuf.wrappers_pb2.StringValue | None = ...,
        created_at: builtins.int = ...,
        is_active: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        schedule: global___WorkflowSchedule | None = ...,
        playbooks: collections.abc.Iterable[protos.playbooks.playbook_pb2.Playbook] | None = ...,
        entry_points: collections.abc.Iterable[global___WorkflowEntryPoint] | None = ...,
        actions: collections.abc.Iterable[global___WorkflowAction] | None = ...,
        last_execution_time: builtins.int = ...,
        last_execution_status: global___WorkflowExecutionStatusType.ValueType = ...,
        configuration: global___WorkflowConfiguration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["configuration", b"configuration", "created_by", b"created_by", "description", b"description", "id", b"id", "is_active", b"is_active", "name", b"name", "schedule", b"schedule"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["actions", b"actions", "configuration", b"configuration", "created_at", b"created_at", "created_by", b"created_by", "description", b"description", "entry_points", b"entry_points", "id", b"id", "is_active", b"is_active", "last_execution_status", b"last_execution_status", "last_execution_time", b"last_execution_time", "name", b"name", "playbooks", b"playbooks", "schedule", b"schedule"]) -> None: ...

global___Workflow = Workflow

@typing_extensions.final
class UpdateWorkflowOp(google.protobuf.message.Message):
    """/////////////////// Workflow Update Ops Proto /////////////////////"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Op:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _OpEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[UpdateWorkflowOp._Op.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: UpdateWorkflowOp._Op.ValueType  # 0
        UPDATE_WORKFLOW_NAME: UpdateWorkflowOp._Op.ValueType  # 1
        UPDATE_WORKFLOW_STATUS: UpdateWorkflowOp._Op.ValueType  # 2
        UPDATE_WORKFLOW: UpdateWorkflowOp._Op.ValueType  # 3
        UPDATE_WORKFLOW_ENTRY_POINT_STATUS: UpdateWorkflowOp._Op.ValueType  # 4
        UPDATE_WORKFLOW_ACTION_STATUS: UpdateWorkflowOp._Op.ValueType  # 5
        UPDATE_WORKFLOW_PLAYBOOK_STATUS: UpdateWorkflowOp._Op.ValueType  # 6

    class Op(_Op, metaclass=_OpEnumTypeWrapper): ...
    UNKNOWN: UpdateWorkflowOp.Op.ValueType  # 0
    UPDATE_WORKFLOW_NAME: UpdateWorkflowOp.Op.ValueType  # 1
    UPDATE_WORKFLOW_STATUS: UpdateWorkflowOp.Op.ValueType  # 2
    UPDATE_WORKFLOW: UpdateWorkflowOp.Op.ValueType  # 3
    UPDATE_WORKFLOW_ENTRY_POINT_STATUS: UpdateWorkflowOp.Op.ValueType  # 4
    UPDATE_WORKFLOW_ACTION_STATUS: UpdateWorkflowOp.Op.ValueType  # 5
    UPDATE_WORKFLOW_PLAYBOOK_STATUS: UpdateWorkflowOp.Op.ValueType  # 6

    @typing_extensions.final
    class UpdateWorkflowName(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NAME_FIELD_NUMBER: builtins.int
        @property
        def name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        def __init__(
            self,
            *,
            name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["name", b"name"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

    @typing_extensions.final
    class UpdateWorkflowStatus(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        IS_ACTIVE_FIELD_NUMBER: builtins.int
        @property
        def is_active(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
        def __init__(
            self,
            *,
            is_active: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["is_active", b"is_active"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["is_active", b"is_active"]) -> None: ...

    @typing_extensions.final
    class UpdateWorkflow(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        WORKFLOW_FIELD_NUMBER: builtins.int
        @property
        def workflow(self) -> global___Workflow: ...
        def __init__(
            self,
            *,
            workflow: global___Workflow | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["workflow", b"workflow"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["workflow", b"workflow"]) -> None: ...

    @typing_extensions.final
    class UpdateWorkflowEntryPointStatus(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ENTRY_POINT_ID_FIELD_NUMBER: builtins.int
        IS_ACTIVE_FIELD_NUMBER: builtins.int
        @property
        def entry_point_id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
        @property
        def is_active(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
        def __init__(
            self,
            *,
            entry_point_id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
            is_active: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["entry_point_id", b"entry_point_id", "is_active", b"is_active"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["entry_point_id", b"entry_point_id", "is_active", b"is_active"]) -> None: ...

    @typing_extensions.final
    class UpdateWorkflowActionStatus(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ACTION_ID_FIELD_NUMBER: builtins.int
        IS_ACTIVE_FIELD_NUMBER: builtins.int
        @property
        def action_id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
        @property
        def is_active(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
        def __init__(
            self,
            *,
            action_id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
            is_active: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["action_id", b"action_id", "is_active", b"is_active"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["action_id", b"action_id", "is_active", b"is_active"]) -> None: ...

    @typing_extensions.final
    class UpdateWorkflowPlaybookStatus(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PLAYBOOK_ID_FIELD_NUMBER: builtins.int
        IS_ACTIVE_FIELD_NUMBER: builtins.int
        @property
        def playbook_id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
        @property
        def is_active(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
        def __init__(
            self,
            *,
            playbook_id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
            is_active: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["is_active", b"is_active", "playbook_id", b"playbook_id"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["is_active", b"is_active", "playbook_id", b"playbook_id"]) -> None: ...

    OP_FIELD_NUMBER: builtins.int
    UPDATE_WORKFLOW_NAME_FIELD_NUMBER: builtins.int
    UPDATE_WORKFLOW_STATUS_FIELD_NUMBER: builtins.int
    UPDATE_WORKFLOW_FIELD_NUMBER: builtins.int
    UPDATE_WORKFLOW_ENTRY_POINT_STATUS_FIELD_NUMBER: builtins.int
    UPDATE_WORKFLOW_ACTION_STATUS_FIELD_NUMBER: builtins.int
    UPDATE_WORKFLOW_PLAYBOOK_STATUS_FIELD_NUMBER: builtins.int
    op: global___UpdateWorkflowOp.Op.ValueType
    @property
    def update_workflow_name(self) -> global___UpdateWorkflowOp.UpdateWorkflowName: ...
    @property
    def update_workflow_status(self) -> global___UpdateWorkflowOp.UpdateWorkflowStatus: ...
    @property
    def update_workflow(self) -> global___UpdateWorkflowOp.UpdateWorkflow: ...
    @property
    def update_workflow_entry_point_status(self) -> global___UpdateWorkflowOp.UpdateWorkflowEntryPointStatus: ...
    @property
    def update_workflow_action_status(self) -> global___UpdateWorkflowOp.UpdateWorkflowActionStatus: ...
    @property
    def update_workflow_playbook_status(self) -> global___UpdateWorkflowOp.UpdateWorkflowPlaybookStatus: ...
    def __init__(
        self,
        *,
        op: global___UpdateWorkflowOp.Op.ValueType = ...,
        update_workflow_name: global___UpdateWorkflowOp.UpdateWorkflowName | None = ...,
        update_workflow_status: global___UpdateWorkflowOp.UpdateWorkflowStatus | None = ...,
        update_workflow: global___UpdateWorkflowOp.UpdateWorkflow | None = ...,
        update_workflow_entry_point_status: global___UpdateWorkflowOp.UpdateWorkflowEntryPointStatus | None = ...,
        update_workflow_action_status: global___UpdateWorkflowOp.UpdateWorkflowActionStatus | None = ...,
        update_workflow_playbook_status: global___UpdateWorkflowOp.UpdateWorkflowPlaybookStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update", b"update", "update_workflow", b"update_workflow", "update_workflow_action_status", b"update_workflow_action_status", "update_workflow_entry_point_status", b"update_workflow_entry_point_status", "update_workflow_name", b"update_workflow_name", "update_workflow_playbook_status", b"update_workflow_playbook_status", "update_workflow_status", b"update_workflow_status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["op", b"op", "update", b"update", "update_workflow", b"update_workflow", "update_workflow_action_status", b"update_workflow_action_status", "update_workflow_entry_point_status", b"update_workflow_entry_point_status", "update_workflow_name", b"update_workflow_name", "update_workflow_playbook_status", b"update_workflow_playbook_status", "update_workflow_status", b"update_workflow_status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["update", b"update"]) -> typing_extensions.Literal["update_workflow_name", "update_workflow_status", "update_workflow", "update_workflow_entry_point_status", "update_workflow_action_status", "update_workflow_playbook_status"] | None: ...

global___UpdateWorkflowOp = UpdateWorkflowOp

@typing_extensions.final
class WorkflowExecutionLog(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    PLAYBOOK_EXECUTION_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    @property
    def playbook_execution(self) -> protos.playbooks.playbook_pb2.PlaybookExecution: ...
    created_at: builtins.int
    def __init__(
        self,
        *,
        id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        playbook_execution: protos.playbooks.playbook_pb2.PlaybookExecution | None = ...,
        created_at: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id", "playbook_execution", b"playbook_execution"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "id", b"id", "playbook_execution", b"playbook_execution"]) -> None: ...

global___WorkflowExecutionLog = WorkflowExecutionLog

@typing_extensions.final
class WorkflowExecution(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    WORKFLOW_RUN_ID_FIELD_NUMBER: builtins.int
    WORKFLOW_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    SCHEDULED_AT_FIELD_NUMBER: builtins.int
    EXPIRY_AT_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    STARTED_AT_FIELD_NUMBER: builtins.int
    FINISHED_AT_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    WORKFLOW_LOGS_FIELD_NUMBER: builtins.int
    EXECUTION_CONFIGURATION_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    @property
    def workflow_run_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def workflow(self) -> global___Workflow: ...
    status: global___WorkflowExecutionStatusType.ValueType
    scheduled_at: builtins.int
    expiry_at: builtins.int
    created_at: builtins.int
    started_at: builtins.int
    finished_at: builtins.int
    @property
    def created_by(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def workflow_logs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WorkflowExecutionLog]: ...
    @property
    def execution_configuration(self) -> global___WorkflowConfiguration: ...
    def __init__(
        self,
        *,
        id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        workflow_run_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        workflow: global___Workflow | None = ...,
        status: global___WorkflowExecutionStatusType.ValueType = ...,
        scheduled_at: builtins.int = ...,
        expiry_at: builtins.int = ...,
        created_at: builtins.int = ...,
        started_at: builtins.int = ...,
        finished_at: builtins.int = ...,
        created_by: google.protobuf.wrappers_pb2.StringValue | None = ...,
        workflow_logs: collections.abc.Iterable[global___WorkflowExecutionLog] | None = ...,
        execution_configuration: global___WorkflowConfiguration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_by", b"created_by", "execution_configuration", b"execution_configuration", "id", b"id", "workflow", b"workflow", "workflow_run_id", b"workflow_run_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "created_by", b"created_by", "execution_configuration", b"execution_configuration", "expiry_at", b"expiry_at", "finished_at", b"finished_at", "id", b"id", "scheduled_at", b"scheduled_at", "started_at", b"started_at", "status", b"status", "workflow", b"workflow", "workflow_logs", b"workflow_logs", "workflow_run_id", b"workflow_run_id"]) -> None: ...

global___WorkflowExecution = WorkflowExecution
