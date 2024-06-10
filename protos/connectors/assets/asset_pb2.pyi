"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import protos.base_pb2
import protos.connectors.assets.azure_asset_pb2
import protos.connectors.assets.clickhouse_asset_pb2
import protos.connectors.assets.cloudwatch_asset_pb2
import protos.connectors.assets.datadog_asset_pb2
import protos.connectors.assets.eks_asset_pb2
import protos.connectors.assets.gke_asset_pb2
import protos.connectors.assets.grafana_asset_pb2
import protos.connectors.assets.newrelic_asset_pb2
import protos.connectors.assets.postgres_asset_pb2
import protos.connectors.assets.remote_server_asset_pb2
import protos.connectors.assets.slack_asset_pb2
import protos.connectors.connector_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ConnectorModelTypeOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODEL_TYPE_FIELD_NUMBER: builtins.int
    CLOUDWATCH_LOG_GROUP_MODEL_OPTIONS_FIELD_NUMBER: builtins.int
    CLOUDWATCH_METRIC_MODEL_OPTIONS_FIELD_NUMBER: builtins.int
    GRAFANA_TARGET_METRIC_PROMQL_MODEL_OPTIONS_FIELD_NUMBER: builtins.int
    CLICKHOUSE_DATABASE_MODEL_OPTIONS_FIELD_NUMBER: builtins.int
    SLACK_CHANNEL_MODEL_OPTIONS_FIELD_NUMBER: builtins.int
    NEW_RELIC_ENTITY_APPLICATION_MODEL_OPTIONS_FIELD_NUMBER: builtins.int
    NEW_RELIC_ENTITY_DASHBOARD_MODEL_OPTIONS_FIELD_NUMBER: builtins.int
    DATADOG_SERVICE_MODEL_OPTIONS_FIELD_NUMBER: builtins.int
    POSTGRES_DATABASE_MODEL_OPTIONS_FIELD_NUMBER: builtins.int
    EKS_CLUSTER_MODEL_OPTIONS_FIELD_NUMBER: builtins.int
    SSH_SERVER_MODEL_OPTIONS_FIELD_NUMBER: builtins.int
    AZURE_WORKSPACE_MODEL_OPTIONS_FIELD_NUMBER: builtins.int
    GRAFANA_PROMETHEUS_DATASOURCE_MODEL_OPTIONS_FIELD_NUMBER: builtins.int
    GKE_CLUSTER_MODEL_OPTIONS_FIELD_NUMBER: builtins.int
    model_type: protos.base_pb2.SourceModelType.ValueType
    @property
    def cloudwatch_log_group_model_options(self) -> protos.connectors.assets.cloudwatch_asset_pb2.CloudwatchLogGroupAssetOptions: ...
    @property
    def cloudwatch_metric_model_options(self) -> protos.connectors.assets.cloudwatch_asset_pb2.CloudwatchMetricAssetOptions: ...
    @property
    def grafana_target_metric_promql_model_options(self) -> protos.connectors.assets.grafana_asset_pb2.GrafanaTargetMetricPromQlAssetOptions: ...
    @property
    def clickhouse_database_model_options(self) -> protos.connectors.assets.clickhouse_asset_pb2.ClickhouseDatabaseAssetOptions: ...
    @property
    def slack_channel_model_options(self) -> protos.connectors.assets.slack_asset_pb2.SlackChannelAssetOptions: ...
    @property
    def new_relic_entity_application_model_options(self) -> protos.connectors.assets.newrelic_asset_pb2.NewRelicApplicationEntityAssetOptions: ...
    @property
    def new_relic_entity_dashboard_model_options(self) -> protos.connectors.assets.newrelic_asset_pb2.NewRelicDashboardEntityAssetOptions: ...
    @property
    def datadog_service_model_options(self) -> protos.connectors.assets.datadog_asset_pb2.DatadogServiceAssetOptions: ...
    @property
    def postgres_database_model_options(self) -> protos.connectors.assets.postgres_asset_pb2.PostgresDatabaseAssetOptions: ...
    @property
    def eks_cluster_model_options(self) -> protos.connectors.assets.eks_asset_pb2.EksClusterAssetOptions: ...
    @property
    def ssh_server_model_options(self) -> protos.connectors.assets.remote_server_asset_pb2.SshServerAssetOptions: ...
    @property
    def azure_workspace_model_options(self) -> protos.connectors.assets.azure_asset_pb2.AzureWorkspaceAssetOptions: ...
    @property
    def grafana_prometheus_datasource_model_options(self) -> protos.connectors.assets.grafana_asset_pb2.GrafanaDatasourceAssetOptions: ...
    @property
    def gke_cluster_model_options(self) -> protos.connectors.assets.gke_asset_pb2.GkeClusterAssetOptions: ...
    def __init__(
        self,
        *,
        model_type: protos.base_pb2.SourceModelType.ValueType = ...,
        cloudwatch_log_group_model_options: protos.connectors.assets.cloudwatch_asset_pb2.CloudwatchLogGroupAssetOptions | None = ...,
        cloudwatch_metric_model_options: protos.connectors.assets.cloudwatch_asset_pb2.CloudwatchMetricAssetOptions | None = ...,
        grafana_target_metric_promql_model_options: protos.connectors.assets.grafana_asset_pb2.GrafanaTargetMetricPromQlAssetOptions | None = ...,
        clickhouse_database_model_options: protos.connectors.assets.clickhouse_asset_pb2.ClickhouseDatabaseAssetOptions | None = ...,
        slack_channel_model_options: protos.connectors.assets.slack_asset_pb2.SlackChannelAssetOptions | None = ...,
        new_relic_entity_application_model_options: protos.connectors.assets.newrelic_asset_pb2.NewRelicApplicationEntityAssetOptions | None = ...,
        new_relic_entity_dashboard_model_options: protos.connectors.assets.newrelic_asset_pb2.NewRelicDashboardEntityAssetOptions | None = ...,
        datadog_service_model_options: protos.connectors.assets.datadog_asset_pb2.DatadogServiceAssetOptions | None = ...,
        postgres_database_model_options: protos.connectors.assets.postgres_asset_pb2.PostgresDatabaseAssetOptions | None = ...,
        eks_cluster_model_options: protos.connectors.assets.eks_asset_pb2.EksClusterAssetOptions | None = ...,
        ssh_server_model_options: protos.connectors.assets.remote_server_asset_pb2.SshServerAssetOptions | None = ...,
        azure_workspace_model_options: protos.connectors.assets.azure_asset_pb2.AzureWorkspaceAssetOptions | None = ...,
        grafana_prometheus_datasource_model_options: protos.connectors.assets.grafana_asset_pb2.GrafanaDatasourceAssetOptions | None = ...,
        gke_cluster_model_options: protos.connectors.assets.gke_asset_pb2.GkeClusterAssetOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["azure_workspace_model_options", b"azure_workspace_model_options", "clickhouse_database_model_options", b"clickhouse_database_model_options", "cloudwatch_log_group_model_options", b"cloudwatch_log_group_model_options", "cloudwatch_metric_model_options", b"cloudwatch_metric_model_options", "datadog_service_model_options", b"datadog_service_model_options", "eks_cluster_model_options", b"eks_cluster_model_options", "gke_cluster_model_options", b"gke_cluster_model_options", "grafana_prometheus_datasource_model_options", b"grafana_prometheus_datasource_model_options", "grafana_target_metric_promql_model_options", b"grafana_target_metric_promql_model_options", "new_relic_entity_application_model_options", b"new_relic_entity_application_model_options", "new_relic_entity_dashboard_model_options", b"new_relic_entity_dashboard_model_options", "options", b"options", "postgres_database_model_options", b"postgres_database_model_options", "slack_channel_model_options", b"slack_channel_model_options", "ssh_server_model_options", b"ssh_server_model_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["azure_workspace_model_options", b"azure_workspace_model_options", "clickhouse_database_model_options", b"clickhouse_database_model_options", "cloudwatch_log_group_model_options", b"cloudwatch_log_group_model_options", "cloudwatch_metric_model_options", b"cloudwatch_metric_model_options", "datadog_service_model_options", b"datadog_service_model_options", "eks_cluster_model_options", b"eks_cluster_model_options", "gke_cluster_model_options", b"gke_cluster_model_options", "grafana_prometheus_datasource_model_options", b"grafana_prometheus_datasource_model_options", "grafana_target_metric_promql_model_options", b"grafana_target_metric_promql_model_options", "model_type", b"model_type", "new_relic_entity_application_model_options", b"new_relic_entity_application_model_options", "new_relic_entity_dashboard_model_options", b"new_relic_entity_dashboard_model_options", "options", b"options", "postgres_database_model_options", b"postgres_database_model_options", "slack_channel_model_options", b"slack_channel_model_options", "ssh_server_model_options", b"ssh_server_model_options"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["options", b"options"]) -> typing_extensions.Literal["cloudwatch_log_group_model_options", "cloudwatch_metric_model_options", "grafana_target_metric_promql_model_options", "clickhouse_database_model_options", "slack_channel_model_options", "new_relic_entity_application_model_options", "new_relic_entity_dashboard_model_options", "datadog_service_model_options", "postgres_database_model_options", "eks_cluster_model_options", "ssh_server_model_options", "azure_workspace_model_options", "grafana_prometheus_datasource_model_options", "gke_cluster_model_options"] | None: ...

global___ConnectorModelTypeOptions = ConnectorModelTypeOptions

@typing_extensions.final
class AccountConnectorAssetsModelOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_TYPE_FIELD_NUMBER: builtins.int
    CONNECTOR_FIELD_NUMBER: builtins.int
    MODEL_TYPES_OPTIONS_FIELD_NUMBER: builtins.int
    connector_type: protos.base_pb2.Source.ValueType
    @property
    def connector(self) -> protos.connectors.connector_pb2.Connector: ...
    @property
    def model_types_options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ConnectorModelTypeOptions]: ...
    def __init__(
        self,
        *,
        connector_type: protos.base_pb2.Source.ValueType = ...,
        connector: protos.connectors.connector_pb2.Connector | None = ...,
        model_types_options: collections.abc.Iterable[global___ConnectorModelTypeOptions] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["connector", b"connector"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["connector", b"connector", "connector_type", b"connector_type", "model_types_options", b"model_types_options"]) -> None: ...

global___AccountConnectorAssetsModelOptions = AccountConnectorAssetsModelOptions

@typing_extensions.final
class AccountConnectorAssetsModelFilters(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLOUDWATCH_LOG_GROUP_MODEL_FILTERS_FIELD_NUMBER: builtins.int
    CLOUDWATCH_METRIC_MODEL_FILTERS_FIELD_NUMBER: builtins.int
    GRAFANA_TARGET_METRIC_PROMQL_MODEL_FILTERS_FIELD_NUMBER: builtins.int
    CLICKHOUSE_DATABASE_MODEL_FILTERS_FIELD_NUMBER: builtins.int
    SLACK_CHANNEL_MODEL_FILTERS_FIELD_NUMBER: builtins.int
    NEW_RELIC_ENTITY_APPLICATION_MODEL_FILTERS_FIELD_NUMBER: builtins.int
    NEW_RELIC_ENTITY_DASHBOARD_MODEL_FILTERS_FIELD_NUMBER: builtins.int
    DATADOG_SERVICE_MODEL_FILTERS_FIELD_NUMBER: builtins.int
    POSTGRES_DATABASE_MODEL_FILTERS_FIELD_NUMBER: builtins.int
    EKS_CLUSTER_MODEL_FILTERS_FIELD_NUMBER: builtins.int
    SSH_SERVER_MODEL_FILTERS_FIELD_NUMBER: builtins.int
    AZURE_WORKSPACE_MODEL_FILTERS_FIELD_NUMBER: builtins.int
    GRAFANA_PROMETHEUS_DATASOURCE_MODEL_FILTERS_FIELD_NUMBER: builtins.int
    GKE_CLUSTER_MODEL_FILTERS_FIELD_NUMBER: builtins.int
    @property
    def cloudwatch_log_group_model_filters(self) -> protos.connectors.assets.cloudwatch_asset_pb2.CloudwatchLogGroupAssetOptions: ...
    @property
    def cloudwatch_metric_model_filters(self) -> protos.connectors.assets.cloudwatch_asset_pb2.CloudwatchMetricAssetOptions: ...
    @property
    def grafana_target_metric_promql_model_filters(self) -> protos.connectors.assets.grafana_asset_pb2.GrafanaTargetMetricPromQlAssetOptions: ...
    @property
    def clickhouse_database_model_filters(self) -> protos.connectors.assets.clickhouse_asset_pb2.ClickhouseDatabaseAssetOptions: ...
    @property
    def slack_channel_model_filters(self) -> protos.connectors.assets.slack_asset_pb2.SlackChannelAssetOptions: ...
    @property
    def new_relic_entity_application_model_filters(self) -> protos.connectors.assets.newrelic_asset_pb2.NewRelicApplicationEntityAssetOptions: ...
    @property
    def new_relic_entity_dashboard_model_filters(self) -> protos.connectors.assets.newrelic_asset_pb2.NewRelicDashboardEntityAssetOptions: ...
    @property
    def datadog_service_model_filters(self) -> protos.connectors.assets.datadog_asset_pb2.DatadogServiceAssetOptions: ...
    @property
    def postgres_database_model_filters(self) -> protos.connectors.assets.postgres_asset_pb2.PostgresDatabaseAssetOptions: ...
    @property
    def eks_cluster_model_filters(self) -> protos.connectors.assets.eks_asset_pb2.EksClusterAssetOptions: ...
    @property
    def ssh_server_model_filters(self) -> protos.connectors.assets.remote_server_asset_pb2.SshServerAssetOptions: ...
    @property
    def azure_workspace_model_filters(self) -> protos.connectors.assets.azure_asset_pb2.AzureWorkspaceAssetOptions: ...
    @property
    def grafana_prometheus_datasource_model_filters(self) -> protos.connectors.assets.grafana_asset_pb2.GrafanaDatasourceAssetOptions: ...
    @property
    def gke_cluster_model_filters(self) -> protos.connectors.assets.gke_asset_pb2.GkeClusterAssetOptions: ...
    def __init__(
        self,
        *,
        cloudwatch_log_group_model_filters: protos.connectors.assets.cloudwatch_asset_pb2.CloudwatchLogGroupAssetOptions | None = ...,
        cloudwatch_metric_model_filters: protos.connectors.assets.cloudwatch_asset_pb2.CloudwatchMetricAssetOptions | None = ...,
        grafana_target_metric_promql_model_filters: protos.connectors.assets.grafana_asset_pb2.GrafanaTargetMetricPromQlAssetOptions | None = ...,
        clickhouse_database_model_filters: protos.connectors.assets.clickhouse_asset_pb2.ClickhouseDatabaseAssetOptions | None = ...,
        slack_channel_model_filters: protos.connectors.assets.slack_asset_pb2.SlackChannelAssetOptions | None = ...,
        new_relic_entity_application_model_filters: protos.connectors.assets.newrelic_asset_pb2.NewRelicApplicationEntityAssetOptions | None = ...,
        new_relic_entity_dashboard_model_filters: protos.connectors.assets.newrelic_asset_pb2.NewRelicDashboardEntityAssetOptions | None = ...,
        datadog_service_model_filters: protos.connectors.assets.datadog_asset_pb2.DatadogServiceAssetOptions | None = ...,
        postgres_database_model_filters: protos.connectors.assets.postgres_asset_pb2.PostgresDatabaseAssetOptions | None = ...,
        eks_cluster_model_filters: protos.connectors.assets.eks_asset_pb2.EksClusterAssetOptions | None = ...,
        ssh_server_model_filters: protos.connectors.assets.remote_server_asset_pb2.SshServerAssetOptions | None = ...,
        azure_workspace_model_filters: protos.connectors.assets.azure_asset_pb2.AzureWorkspaceAssetOptions | None = ...,
        grafana_prometheus_datasource_model_filters: protos.connectors.assets.grafana_asset_pb2.GrafanaDatasourceAssetOptions | None = ...,
        gke_cluster_model_filters: protos.connectors.assets.gke_asset_pb2.GkeClusterAssetOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["azure_workspace_model_filters", b"azure_workspace_model_filters", "clickhouse_database_model_filters", b"clickhouse_database_model_filters", "cloudwatch_log_group_model_filters", b"cloudwatch_log_group_model_filters", "cloudwatch_metric_model_filters", b"cloudwatch_metric_model_filters", "datadog_service_model_filters", b"datadog_service_model_filters", "eks_cluster_model_filters", b"eks_cluster_model_filters", "filters", b"filters", "gke_cluster_model_filters", b"gke_cluster_model_filters", "grafana_prometheus_datasource_model_filters", b"grafana_prometheus_datasource_model_filters", "grafana_target_metric_promql_model_filters", b"grafana_target_metric_promql_model_filters", "new_relic_entity_application_model_filters", b"new_relic_entity_application_model_filters", "new_relic_entity_dashboard_model_filters", b"new_relic_entity_dashboard_model_filters", "postgres_database_model_filters", b"postgres_database_model_filters", "slack_channel_model_filters", b"slack_channel_model_filters", "ssh_server_model_filters", b"ssh_server_model_filters"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["azure_workspace_model_filters", b"azure_workspace_model_filters", "clickhouse_database_model_filters", b"clickhouse_database_model_filters", "cloudwatch_log_group_model_filters", b"cloudwatch_log_group_model_filters", "cloudwatch_metric_model_filters", b"cloudwatch_metric_model_filters", "datadog_service_model_filters", b"datadog_service_model_filters", "eks_cluster_model_filters", b"eks_cluster_model_filters", "filters", b"filters", "gke_cluster_model_filters", b"gke_cluster_model_filters", "grafana_prometheus_datasource_model_filters", b"grafana_prometheus_datasource_model_filters", "grafana_target_metric_promql_model_filters", b"grafana_target_metric_promql_model_filters", "new_relic_entity_application_model_filters", b"new_relic_entity_application_model_filters", "new_relic_entity_dashboard_model_filters", b"new_relic_entity_dashboard_model_filters", "postgres_database_model_filters", b"postgres_database_model_filters", "slack_channel_model_filters", b"slack_channel_model_filters", "ssh_server_model_filters", b"ssh_server_model_filters"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["filters", b"filters"]) -> typing_extensions.Literal["cloudwatch_log_group_model_filters", "cloudwatch_metric_model_filters", "grafana_target_metric_promql_model_filters", "clickhouse_database_model_filters", "slack_channel_model_filters", "new_relic_entity_application_model_filters", "new_relic_entity_dashboard_model_filters", "datadog_service_model_filters", "postgres_database_model_filters", "eks_cluster_model_filters", "ssh_server_model_filters", "azure_workspace_model_filters", "grafana_prometheus_datasource_model_filters", "gke_cluster_model_filters"] | None: ...

global___AccountConnectorAssetsModelFilters = AccountConnectorAssetsModelFilters

@typing_extensions.final
class AccountConnectorAssets(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTOR_FIELD_NUMBER: builtins.int
    CLOUDWATCH_FIELD_NUMBER: builtins.int
    GRAFANA_FIELD_NUMBER: builtins.int
    CLICKHOUSE_FIELD_NUMBER: builtins.int
    SLACK_FIELD_NUMBER: builtins.int
    NEW_RELIC_FIELD_NUMBER: builtins.int
    DATADOG_FIELD_NUMBER: builtins.int
    POSTGRES_FIELD_NUMBER: builtins.int
    EKS_FIELD_NUMBER: builtins.int
    REMOTE_SERVER_FIELD_NUMBER: builtins.int
    AZURE_FIELD_NUMBER: builtins.int
    GKE_FIELD_NUMBER: builtins.int
    @property
    def connector(self) -> protos.connectors.connector_pb2.Connector: ...
    @property
    def cloudwatch(self) -> protos.connectors.assets.cloudwatch_asset_pb2.CloudwatchAssets: ...
    @property
    def grafana(self) -> protos.connectors.assets.grafana_asset_pb2.GrafanaAssets: ...
    @property
    def clickhouse(self) -> protos.connectors.assets.clickhouse_asset_pb2.ClickhouseAssets: ...
    @property
    def slack(self) -> protos.connectors.assets.slack_asset_pb2.SlackAssets: ...
    @property
    def new_relic(self) -> protos.connectors.assets.newrelic_asset_pb2.NewRelicAssets: ...
    @property
    def datadog(self) -> protos.connectors.assets.datadog_asset_pb2.DatadogAssets: ...
    @property
    def postgres(self) -> protos.connectors.assets.postgres_asset_pb2.PostgresAssets: ...
    @property
    def eks(self) -> protos.connectors.assets.eks_asset_pb2.EksAssets: ...
    @property
    def remote_server(self) -> protos.connectors.assets.remote_server_asset_pb2.RemoteServerAssets: ...
    @property
    def azure(self) -> protos.connectors.assets.azure_asset_pb2.AzureAssets: ...
    @property
    def gke(self) -> protos.connectors.assets.gke_asset_pb2.GkeAssets: ...
    def __init__(
        self,
        *,
        connector: protos.connectors.connector_pb2.Connector | None = ...,
        cloudwatch: protos.connectors.assets.cloudwatch_asset_pb2.CloudwatchAssets | None = ...,
        grafana: protos.connectors.assets.grafana_asset_pb2.GrafanaAssets | None = ...,
        clickhouse: protos.connectors.assets.clickhouse_asset_pb2.ClickhouseAssets | None = ...,
        slack: protos.connectors.assets.slack_asset_pb2.SlackAssets | None = ...,
        new_relic: protos.connectors.assets.newrelic_asset_pb2.NewRelicAssets | None = ...,
        datadog: protos.connectors.assets.datadog_asset_pb2.DatadogAssets | None = ...,
        postgres: protos.connectors.assets.postgres_asset_pb2.PostgresAssets | None = ...,
        eks: protos.connectors.assets.eks_asset_pb2.EksAssets | None = ...,
        remote_server: protos.connectors.assets.remote_server_asset_pb2.RemoteServerAssets | None = ...,
        azure: protos.connectors.assets.azure_asset_pb2.AzureAssets | None = ...,
        gke: protos.connectors.assets.gke_asset_pb2.GkeAssets | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["assets", b"assets", "azure", b"azure", "clickhouse", b"clickhouse", "cloudwatch", b"cloudwatch", "connector", b"connector", "datadog", b"datadog", "eks", b"eks", "gke", b"gke", "grafana", b"grafana", "new_relic", b"new_relic", "postgres", b"postgres", "remote_server", b"remote_server", "slack", b"slack"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assets", b"assets", "azure", b"azure", "clickhouse", b"clickhouse", "cloudwatch", b"cloudwatch", "connector", b"connector", "datadog", b"datadog", "eks", b"eks", "gke", b"gke", "grafana", b"grafana", "new_relic", b"new_relic", "postgres", b"postgres", "remote_server", b"remote_server", "slack", b"slack"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["assets", b"assets"]) -> typing_extensions.Literal["cloudwatch", "grafana", "clickhouse", "slack", "new_relic", "datadog", "postgres", "eks", "remote_server", "azure", "gke"] | None: ...

global___AccountConnectorAssets = AccountConnectorAssets
