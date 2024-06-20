"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class PagerDutyIncidentEntryPoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PD_INCIDENT_ID_FIELD_NUMBER: builtins.int
    PD_INCIDENT_TITLE_FIELD_NUMBER: builtins.int
    PD_SERVICE_ID_FIELD_NUMBER: builtins.int
    @property
    def pd_incident_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def pd_incident_title(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def pd_service_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        pd_incident_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        pd_incident_title: google.protobuf.wrappers_pb2.StringValue | None = ...,
        pd_service_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pd_incident_id", b"pd_incident_id", "pd_incident_title", b"pd_incident_title", "pd_service_id", b"pd_service_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pd_incident_id", b"pd_incident_id", "pd_incident_title", b"pd_incident_title", "pd_service_id", b"pd_service_id"]) -> None: ...

global___PagerDutyIncidentEntryPoint = PagerDutyIncidentEntryPoint
