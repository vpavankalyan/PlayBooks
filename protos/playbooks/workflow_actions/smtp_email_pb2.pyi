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
class SMTPEmailWorkflowAction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TO_EMAIL_FIELD_NUMBER: builtins.int
    SUBJECT_FIELD_NUMBER: builtins.int
    @property
    def to_email(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def subject(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        to_email: google.protobuf.wrappers_pb2.StringValue | None = ...,
        subject: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["subject", b"subject", "to_email", b"to_email"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["subject", b"subject", "to_email", b"to_email"]) -> None: ...

global___SMTPEmailWorkflowAction = SMTPEmailWorkflowAction