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
import protos.base_pb2
import protos.connectors.connector_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class NewRelicApplicationEntityAssetModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class GoldenMetric(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        GOLDEN_METRIC_NAME_FIELD_NUMBER: builtins.int
        GOLDEN_METRIC_UNIT_FIELD_NUMBER: builtins.int
        GOLDEN_METRIC_NRQL_EXPRESSION_FIELD_NUMBER: builtins.int
        @property
        def golden_metric_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def golden_metric_unit(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def golden_metric_nrql_expression(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        def __init__(
            self,
            *,
            golden_metric_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
            golden_metric_unit: google.protobuf.wrappers_pb2.StringValue | None = ...,
            golden_metric_nrql_expression: google.protobuf.wrappers_pb2.StringValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["golden_metric_name", b"golden_metric_name", "golden_metric_nrql_expression", b"golden_metric_nrql_expression", "golden_metric_unit", b"golden_metric_unit"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["golden_metric_name", b"golden_metric_name", "golden_metric_nrql_expression", b"golden_metric_nrql_expression", "golden_metric_unit", b"golden_metric_unit"]) -> None: ...

    APPLICATION_ENTITY_GUID_FIELD_NUMBER: builtins.int
    APPLICATION_NAME_FIELD_NUMBER: builtins.int
    GOLDEN_METRICS_FIELD_NUMBER: builtins.int
    @property
    def application_entity_guid(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def application_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def golden_metrics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NewRelicApplicationEntityAssetModel.GoldenMetric]: ...
    def __init__(
        self,
        *,
        application_entity_guid: google.protobuf.wrappers_pb2.StringValue | None = ...,
        application_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        golden_metrics: collections.abc.Iterable[global___NewRelicApplicationEntityAssetModel.GoldenMetric] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["application_entity_guid", b"application_entity_guid", "application_name", b"application_name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["application_entity_guid", b"application_entity_guid", "application_name", b"application_name", "golden_metrics", b"golden_metrics"]) -> None: ...

global___NewRelicApplicationEntityAssetModel = NewRelicApplicationEntityAssetModel

@typing_extensions.final
class NewRelicApplicationEntityAssetOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    APPLICATION_NAMES_FIELD_NUMBER: builtins.int
    @property
    def application_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        application_names: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["application_names", b"application_names"]) -> None: ...

global___NewRelicApplicationEntityAssetOptions = NewRelicApplicationEntityAssetOptions

@typing_extensions.final
class NewRelicDashboardEntityAssetModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class PageWidget(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        WIDGET_ID_FIELD_NUMBER: builtins.int
        WIDGET_TITLE_FIELD_NUMBER: builtins.int
        WIDGET_TYPE_FIELD_NUMBER: builtins.int
        WIDGET_NRQL_EXPRESSION_FIELD_NUMBER: builtins.int
        @property
        def widget_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def widget_title(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def widget_type(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def widget_nrql_expression(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        def __init__(
            self,
            *,
            widget_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
            widget_title: google.protobuf.wrappers_pb2.StringValue | None = ...,
            widget_type: google.protobuf.wrappers_pb2.StringValue | None = ...,
            widget_nrql_expression: google.protobuf.wrappers_pb2.StringValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["widget_id", b"widget_id", "widget_nrql_expression", b"widget_nrql_expression", "widget_title", b"widget_title", "widget_type", b"widget_type"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["widget_id", b"widget_id", "widget_nrql_expression", b"widget_nrql_expression", "widget_title", b"widget_title", "widget_type", b"widget_type"]) -> None: ...

    @typing_extensions.final
    class DashboardPage(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PAGE_GUID_FIELD_NUMBER: builtins.int
        PAGE_NAME_FIELD_NUMBER: builtins.int
        WIDGETS_FIELD_NUMBER: builtins.int
        @property
        def page_guid(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def page_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def widgets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NewRelicDashboardEntityAssetModel.PageWidget]: ...
        def __init__(
            self,
            *,
            page_guid: google.protobuf.wrappers_pb2.StringValue | None = ...,
            page_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
            widgets: collections.abc.Iterable[global___NewRelicDashboardEntityAssetModel.PageWidget] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["page_guid", b"page_guid", "page_name", b"page_name"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["page_guid", b"page_guid", "page_name", b"page_name", "widgets", b"widgets"]) -> None: ...

    DASHBOARD_GUID_FIELD_NUMBER: builtins.int
    DASHBOARD_NAME_FIELD_NUMBER: builtins.int
    PAGES_FIELD_NUMBER: builtins.int
    @property
    def dashboard_guid(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def dashboard_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def pages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NewRelicDashboardEntityAssetModel.DashboardPage]: ...
    def __init__(
        self,
        *,
        dashboard_guid: google.protobuf.wrappers_pb2.StringValue | None = ...,
        dashboard_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        pages: collections.abc.Iterable[global___NewRelicDashboardEntityAssetModel.DashboardPage] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dashboard_guid", b"dashboard_guid", "dashboard_name", b"dashboard_name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dashboard_guid", b"dashboard_guid", "dashboard_name", b"dashboard_name", "pages", b"pages"]) -> None: ...

global___NewRelicDashboardEntityAssetModel = NewRelicDashboardEntityAssetModel

@typing_extensions.final
class NewRelicDashboardEntityAssetOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class DashboardOptions(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing_extensions.final
        class DashboardPageOptions(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            PAGE_GUID_FIELD_NUMBER: builtins.int
            PAGE_NAME_FIELD_NUMBER: builtins.int
            @property
            def page_guid(self) -> google.protobuf.wrappers_pb2.StringValue: ...
            @property
            def page_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
            def __init__(
                self,
                *,
                page_guid: google.protobuf.wrappers_pb2.StringValue | None = ...,
                page_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["page_guid", b"page_guid", "page_name", b"page_name"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["page_guid", b"page_guid", "page_name", b"page_name"]) -> None: ...

        DASHBOARD_GUID_FIELD_NUMBER: builtins.int
        DASHBOARD_NAME_FIELD_NUMBER: builtins.int
        PAGE_OPTIONS_FIELD_NUMBER: builtins.int
        @property
        def dashboard_guid(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def dashboard_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def page_options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NewRelicDashboardEntityAssetOptions.DashboardOptions.DashboardPageOptions]: ...
        def __init__(
            self,
            *,
            dashboard_guid: google.protobuf.wrappers_pb2.StringValue | None = ...,
            dashboard_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
            page_options: collections.abc.Iterable[global___NewRelicDashboardEntityAssetOptions.DashboardOptions.DashboardPageOptions] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["dashboard_guid", b"dashboard_guid", "dashboard_name", b"dashboard_name"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["dashboard_guid", b"dashboard_guid", "dashboard_name", b"dashboard_name", "page_options", b"page_options"]) -> None: ...

    DASHBOARDS_FIELD_NUMBER: builtins.int
    @property
    def dashboards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NewRelicDashboardEntityAssetOptions.DashboardOptions]: ...
    def __init__(
        self,
        *,
        dashboards: collections.abc.Iterable[global___NewRelicDashboardEntityAssetOptions.DashboardOptions] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dashboards", b"dashboards"]) -> None: ...

global___NewRelicDashboardEntityAssetOptions = NewRelicDashboardEntityAssetOptions

@typing_extensions.final
class NewRelicAssetModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    CONNECTOR_TYPE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    LAST_UPDATED_FIELD_NUMBER: builtins.int
    NEW_RELIC_ENTITY_APPLICATION_FIELD_NUMBER: builtins.int
    NEW_RELIC_ENTITY_DASHBOARD_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    connector_type: protos.base_pb2.Source.ValueType
    type: protos.connectors.connector_pb2.ConnectorMetadataModelType.ValueType
    last_updated: builtins.int
    @property
    def new_relic_entity_application(self) -> global___NewRelicApplicationEntityAssetModel: ...
    @property
    def new_relic_entity_dashboard(self) -> global___NewRelicDashboardEntityAssetModel: ...
    def __init__(
        self,
        *,
        id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        connector_type: protos.base_pb2.Source.ValueType = ...,
        type: protos.connectors.connector_pb2.ConnectorMetadataModelType.ValueType = ...,
        last_updated: builtins.int = ...,
        new_relic_entity_application: global___NewRelicApplicationEntityAssetModel | None = ...,
        new_relic_entity_dashboard: global___NewRelicDashboardEntityAssetModel | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["asset", b"asset", "id", b"id", "new_relic_entity_application", b"new_relic_entity_application", "new_relic_entity_dashboard", b"new_relic_entity_dashboard"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset", b"asset", "connector_type", b"connector_type", "id", b"id", "last_updated", b"last_updated", "new_relic_entity_application", b"new_relic_entity_application", "new_relic_entity_dashboard", b"new_relic_entity_dashboard", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["asset", b"asset"]) -> typing_extensions.Literal["new_relic_entity_application", "new_relic_entity_dashboard"] | None: ...

global___NewRelicAssetModel = NewRelicAssetModel

@typing_extensions.final
class NewRelicAssets(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ASSETS_FIELD_NUMBER: builtins.int
    @property
    def assets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NewRelicAssetModel]: ...
    def __init__(
        self,
        *,
        assets: collections.abc.Iterable[global___NewRelicAssetModel] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["assets", b"assets"]) -> None: ...

global___NewRelicAssets = NewRelicAssets
