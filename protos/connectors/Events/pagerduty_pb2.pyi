"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class PagerDutyIncidentModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INCIDENT_ID_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    SERVICE_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    @property
    def incident_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def title(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def service_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def created_at(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        incident_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        title: google.protobuf.wrappers_pb2.StringValue | None = ...,
        service_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        created_at: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "incident_id", b"incident_id", "service_id", b"service_id", "title", b"title"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "incident_id", b"incident_id", "service_id", b"service_id", "title", b"title"]) -> None: ...

global___PagerDutyIncidentModel = PagerDutyIncidentModel

@typing_extensions.final
class PagerDutyAlertModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALERT_ID_FIELD_NUMBER: builtins.int
    INCIDENT_ID_FIELD_NUMBER: builtins.int
    SUMMARY_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    @property
    def alert_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def incident_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def summary(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def body(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        alert_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        incident_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        summary: google.protobuf.wrappers_pb2.StringValue | None = ...,
        body: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["alert_id", b"alert_id", "body", b"body", "incident_id", b"incident_id", "summary", b"summary"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["alert_id", b"alert_id", "body", b"body", "incident_id", b"incident_id", "summary", b"summary"]) -> None: ...

global___PagerDutyAlertModel = PagerDutyAlertModel

@typing_extensions.final
class PagerDutyAssets(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INCIDENTS_FIELD_NUMBER: builtins.int
    ALERTS_FIELD_NUMBER: builtins.int
    @property
    def incidents(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PagerDutyIncidentModel]: ...
    @property
    def alerts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PagerDutyAlertModel]: ...
    def __init__(
        self,
        *,
        incidents: collections.abc.Iterable[global___PagerDutyIncidentModel] | None = ...,
        alerts: collections.abc.Iterable[global___PagerDutyAlertModel] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["alerts", b"alerts", "incidents", b"incidents"]) -> None: ...

global___PagerDutyAssets = PagerDutyAssets