from datetime import timezone
from django.contrib.sites.models import Site as DjangoSite
from django.db import models

from protos.base_pb2 import Source, SourceKeyType, SourceModelType
from utils.model_utils import generate_choices

from google.protobuf.wrappers_pb2 import StringValue, BoolValue, UInt64Value

from accounts.models import Account

from protos.connectors.connector_pb2 import Connector as ConnectorProto, ConnectorKey as ConnectorKeyProto, \
    PeriodicRunStatus

integrations_connector_type_display_name_map = {
    Source.SLACK: 'SLACK',
    Source.GOOGLE_CHAT: 'Google Chat',
    Source.SENTRY: 'SENTRY',
    Source.NEW_RELIC: 'NEW RELIC',
    Source.DATADOG: 'DATADOG',
    Source.DATADOG_OAUTH: 'DATADOG',
    Source.GRAFANA: 'GRAFANA',
    Source.GRAFANA_VPC: 'GRAFANA VPC',
    Source.GITHUB_ACTIONS: 'GITHUB ACTIONS',
    Source.ELASTIC_APM: 'ELASTIC APM',
    Source.VICTORIA_METRICS: 'VictoriaMetrics',
    Source.PROMETHEUS: 'PROMETHEUS',
    Source.CLOUDWATCH: 'CLOUDWATCH',
    Source.GCM: 'GOOGLE CLOUD MONITORING',
    Source.CLICKHOUSE: 'CLICKHOUSE',
    Source.POSTGRES: 'POSTGRES',
    Source.PAGER_DUTY: 'PAGERDUTY',
    Source.OPS_GENIE: 'OPS GENIE',
    Source.EKS: 'EKS KUBERNETES',
    Source.SQL_DATABASE_CONNECTION: 'SQL DATABASE CONNECTION',
    Source.OPEN_AI: 'OPEN AI',
    Source.REMOTE_SERVER: 'REMOTE SERVER',
    Source.GRAFANA_MIMIR: 'GRAFANA MIMIR',
}

integrations_connector_type_category_map = {
    Source.SLACK: 'Alert Channels',
    Source.GOOGLE_CHAT: 'Alert Channels',
    Source.SENTRY: 'APM Tools',
    Source.NEW_RELIC: 'APM Tools',
    Source.DATADOG: 'APM Tools',
    Source.DATADOG_OAUTH: 'APM Tools',
    Source.GRAFANA: 'APM Tools',
    Source.GRAFANA_VPC: 'APM Tools',
    Source.GITHUB_ACTIONS: 'CI/CD',
    Source.ELASTIC_APM: 'APM Tools',
    Source.VICTORIA_METRICS: 'APM Tools',
    Source.PROMETHEUS: 'APM Tools',
    Source.CLOUDWATCH: 'Cloud',
    Source.GCM: 'Cloud',
    Source.CLICKHOUSE: 'Database',
    Source.POSTGRES: 'Database',
    Source.PAGER_DUTY: 'Alert Channels',
    Source.OPS_GENIE: 'Alert Channels',
    Source.EKS: 'Cloud',
    Source.SQL_DATABASE_CONNECTION: 'Database',
    Source.OPEN_AI: 'LLM Tools',
    Source.REMOTE_SERVER: 'Remote Server',
    Source.GRAFANA_MIMIR: 'APM Tools',
}

integrations_connector_type_connector_keys_map = {
    Source.SLACK: [
        [
            SourceKeyType.SLACK_BOT_AUTH_TOKEN,
            SourceKeyType.SLACK_APP_ID
        ]
    ],
    Source.NEW_RELIC: [
        [
            SourceKeyType.NEWRELIC_API_KEY,
            SourceKeyType.NEWRELIC_APP_ID,
            SourceKeyType.NEWRELIC_API_DOMAIN
        ]
    ],
    Source.DATADOG: [
        [
            SourceKeyType.DATADOG_API_KEY,
            SourceKeyType.DATADOG_APP_KEY,
            SourceKeyType.DATADOG_API_DOMAIN
        ]
    ],
    Source.DATADOG_OAUTH: [
        [
            SourceKeyType.DATADOG_AUTH_TOKEN,
            SourceKeyType.DATADOG_API_DOMAIN,
            SourceKeyType.DATADOG_API_KEY
        ]
    ],
    Source.GRAFANA: [
        [
            SourceKeyType.GRAFANA_HOST,
            SourceKeyType.GRAFANA_API_KEY
        ]
    ],
    Source.GRAFANA_VPC: [
        [
            SourceKeyType.AGENT_PROXY_HOST,
            SourceKeyType.AGENT_PROXY_API_KEY
        ]
    ],
    Source.AGENT_PROXY: [
        [
            SourceKeyType.AGENT_PROXY_HOST,
            SourceKeyType.AGENT_PROXY_API_KEY
        ]
    ],
    Source.CLOUDWATCH: [
        [
            SourceKeyType.AWS_ACCESS_KEY,
            SourceKeyType.AWS_SECRET_KEY,
            SourceKeyType.AWS_REGION,
        ]
    ],
    Source.CLICKHOUSE: [
        [
            SourceKeyType.CLICKHOUSE_INTERFACE,
            SourceKeyType.CLICKHOUSE_HOST,
            SourceKeyType.CLICKHOUSE_PORT,
            SourceKeyType.CLICKHOUSE_USER,
            SourceKeyType.CLICKHOUSE_PASSWORD
        ]
    ],
    Source.POSTGRES: [
        [
            SourceKeyType.POSTGRES_HOST,
            SourceKeyType.POSTGRES_USER,
            SourceKeyType.POSTGRES_PASSWORD,
            SourceKeyType.POSTGRES_PORT,
            SourceKeyType.POSTGRES_DATABASE
        ]
    ],
    Source.EKS: [
        [
            SourceKeyType.AWS_ACCESS_KEY,
            SourceKeyType.AWS_SECRET_KEY,
            SourceKeyType.AWS_REGION,
            SourceKeyType.EKS_ROLE_ARN,
        ]
    ],
    Source.SQL_DATABASE_CONNECTION: [
        [
            SourceKeyType.SQL_DATABASE_CONNECTION_STRING_URI,
        ]
    ],
    Source.OPEN_AI: [
        [
            SourceKeyType.OPEN_AI_API_KEY,
        ]
    ],
    Source.GRAFANA_MIMIR: [
        [
            SourceKeyType.MIMIR_HOST,
            SourceKeyType.X_SCOPE_ORG_ID,
        ]
    ],
    Source.REMOTE_SERVER: [
        [
            SourceKeyType.REMOTE_SERVER_USER,
            SourceKeyType.REMOTE_SERVER_HOST,
            SourceKeyType.REMOTE_SERVER_PASSWORD,
            SourceKeyType.REMOTE_SERVER_PEM
        ],
        [
            SourceKeyType.REMOTE_SERVER_USER,
            SourceKeyType.REMOTE_SERVER_HOST,
        ],
        [
            SourceKeyType.REMOTE_SERVER_USER,
            SourceKeyType.REMOTE_SERVER_HOST,
            SourceKeyType.REMOTE_SERVER_PEM
        ],
        [
            SourceKeyType.REMOTE_SERVER_USER,
            SourceKeyType.REMOTE_SERVER_HOST,
            SourceKeyType.REMOTE_SERVER_PASSWORD
        ]
    ]
}

integrations_connector_key_display_name_map = {
    SourceKeyType.SLACK_BOT_AUTH_TOKEN: 'Bot Auth Token',
    SourceKeyType.GOOGLE_CHAT_BOT_OAUTH_TOKEN: 'OAuth Token',
    SourceKeyType.SENTRY_API_KEY: 'API Key',
    SourceKeyType.SENTRY_ORG_SLUG: 'Org Slug',
    SourceKeyType.NEWRELIC_API_KEY: 'API Key',
    SourceKeyType.NEWRELIC_APP_ID: 'Account ID',
    SourceKeyType.NEWRELIC_API_DOMAIN: 'API Domain',
    SourceKeyType.DATADOG_API_KEY: 'API Key',
    SourceKeyType.DATADOG_APP_KEY: 'App Key',
    SourceKeyType.DATADOG_API_DOMAIN: 'API Domain',
    SourceKeyType.DATADOG_AUTH_TOKEN: 'OAuth Token',
    SourceKeyType.GRAFANA_HOST: 'Host',
    SourceKeyType.GRAFANA_API_KEY: 'API Key',
    SourceKeyType.AGENT_PROXY_HOST: 'Doctor Droid Agent Host',
    SourceKeyType.AGENT_PROXY_API_KEY: 'Doctor Droid API Token',
    SourceKeyType.GITHUB_ACTIONS_TOKEN: 'Token',
    SourceKeyType.AWS_ACCESS_KEY: 'AWS Access Key',
    SourceKeyType.AWS_SECRET_KEY: 'AWS Secret Key',
    SourceKeyType.AWS_REGION: 'AWS Region',
    SourceKeyType.GCM_PROJECT_ID: 'Project ID',
    SourceKeyType.GCM_PRIVATE_KEY: 'Private Key',
    SourceKeyType.GCM_CLIENT_EMAIL: 'Client Email',
    SourceKeyType.GCM_TOKEN_URI: 'Token URI',
    SourceKeyType.CLICKHOUSE_INTERFACE: 'Interface',
    SourceKeyType.CLICKHOUSE_HOST: 'Host',
    SourceKeyType.CLICKHOUSE_PORT: 'Port',
    SourceKeyType.CLICKHOUSE_USER: 'User',
    SourceKeyType.CLICKHOUSE_PASSWORD: 'Password',
    SourceKeyType.POSTGRES_HOST: 'Host',
    SourceKeyType.POSTGRES_USER: 'DB User',
    SourceKeyType.POSTGRES_PASSWORD: 'Password',
    SourceKeyType.POSTGRES_PORT: 'Port',
    SourceKeyType.POSTGRES_DATABASE: 'Database',
    SourceKeyType.PAGER_DUTY_API_KEY: 'API Key',
    SourceKeyType.OPS_GENIE_API_KEY: 'API Key',
    SourceKeyType.EKS_ROLE_ARN: 'EKS Role ARN',
    SourceKeyType.SLACK_APP_ID: 'App ID',
    SourceKeyType.SQL_DATABASE_CONNECTION_STRING_URI: 'Sql Database Connection URI',
    SourceKeyType.OPEN_AI_API_KEY: 'API Key',
    SourceKeyType.REMOTE_SERVER_PEM: 'PEM',
    SourceKeyType.REMOTE_SERVER_USER: 'User',
    SourceKeyType.REMOTE_SERVER_HOST: 'Host',
    SourceKeyType.REMOTE_SERVER_PASSWORD: 'Password',
    SourceKeyType.MIMIR_HOST: 'Host',
    SourceKeyType.X_SCOPE_ORG_ID: 'X-Scope-OrgId',
}


class Connector(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=255)
    connector_type = models.IntegerField(null=True, blank=True, choices=generate_choices(Source),
                                         default=Source.UNKNOWN)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    created_by = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = [['account', 'name', 'connector_type']]

    def __str__(self):
        return f'{self.account}:{self.connector_type}:{self.name}'

    @property
    def proto_partial(self) -> ConnectorProto:
        return ConnectorProto(
            id=UInt64Value(value=self.id),
            type=self.connector_type,
            is_active=BoolValue(value=self.is_active),
            name=StringValue(value=self.name),
            created_at=int(self.created_at.replace(tzinfo=timezone.utc).timestamp()),
            updated_at=int(self.updated_at.replace(tzinfo=timezone.utc).timestamp()),
            created_by=StringValue(value=self.created_by),
            display_name=StringValue(value=integrations_connector_type_display_name_map.get(self.connector_type, '')),
            category=StringValue(value=integrations_connector_type_category_map.get(self.connector_type, '')),
        )

    @property
    def proto(self) -> ConnectorProto:
        keys = self.connectorkey_set.filter(is_active=True)
        keys_proto = [key.proto for key in keys]
        return ConnectorProto(
            id=UInt64Value(value=self.id),
            type=self.connector_type,
            is_active=BoolValue(value=self.is_active),
            name=StringValue(value=self.name),
            created_at=int(self.created_at.replace(tzinfo=timezone.utc).timestamp()),
            updated_at=int(self.updated_at.replace(tzinfo=timezone.utc).timestamp()),
            created_by=StringValue(value=self.created_by),
            display_name=StringValue(value=integrations_connector_type_display_name_map.get(self.connector_type, '')),
            category=StringValue(value=integrations_connector_type_category_map.get(self.connector_type, '')),
            keys=keys_proto
        )

    @property
    def unmasked_proto(self) -> ConnectorProto:
        keys = self.connectorkey_set.filter(is_active=True)
        keys_proto = [key.unmasked_proto for key in keys]
        return ConnectorProto(
            id=UInt64Value(value=self.id),
            type=self.connector_type,
            is_active=BoolValue(value=self.is_active),
            name=StringValue(value=self.name),
            created_at=int(self.created_at.replace(tzinfo=timezone.utc).timestamp()),
            updated_at=int(self.updated_at.replace(tzinfo=timezone.utc).timestamp()),
            created_by=StringValue(value=self.created_by),
            display_name=StringValue(value=integrations_connector_type_display_name_map.get(self.connector_type, '')),
            category=StringValue(value=integrations_connector_type_category_map.get(self.connector_type, '')),
            keys=keys_proto
        )


class ConnectorKey(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_index=True)
    connector = models.ForeignKey(Connector, on_delete=models.CASCADE)
    key_type = models.IntegerField(null=True, blank=True, choices=generate_choices(SourceKeyType),
                                   default=SourceKeyType.UNKNOWN_SKT)
    key = models.TextField()
    metadata = models.JSONField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        unique_together = [['account', 'connector', 'key_type', 'key']]

    @property
    def get_proto(self):
        # Hard Coded Key Masking for sensitive keys
        if self.key_type in [ConnectorKeyProto.KeyType.DATADOG_APP_KEY, ConnectorKeyProto.KeyType.DATADOG_API_KEY,
                             ConnectorKeyProto.KeyType.NEWRELIC_API_KEY, ConnectorKeyProto.KeyType.NEWRELIC_APP_ID,
                             ConnectorKeyProto.KeyType.NEWRELIC_QUERY_KEY,
                             ConnectorKeyProto.KeyType.SLACK_BOT_AUTH_TOKEN,
                             ConnectorKeyProto.KeyType.HONEYBADGER_USERNAME,
                             ConnectorKeyProto.KeyType.HONEYBADGER_PASSWORD,
                             ConnectorKeyProto.KeyType.HONEYBADGER_PROJECT_ID, ConnectorKeyProto.KeyType.AWS_ACCESS_KEY,
                             ConnectorKeyProto.KeyType.AWS_SECRET_KEY, ConnectorKeyProto.KeyType.DATADOG_AUTH_TOKEN,
                             ConnectorKeyProto.KeyType.GOOGLE_CHAT_BOT_OAUTH_TOKEN,
                             ConnectorKeyProto.KeyType.GRAFANA_API_KEY,
                             ConnectorKeyProto.KeyType.AGENT_PROXY_API_KEY,
                             ConnectorKeyProto.KeyType.GITHUB_ACTIONS_TOKEN,
                             ConnectorKeyProto.KeyType.AGENT_PROXY_HOST,
                             ConnectorKeyProto.KeyType.AWS_ASSUMED_ROLE_ARN,
                             ConnectorKeyProto.KeyType.CLICKHOUSE_USER, ConnectorKeyProto.KeyType.CLICKHOUSE_PASSWORD,
                             ConnectorKeyProto.KeyType.GCM_PROJECT_ID, ConnectorKeyProto.KeyType.GCM_PRIVATE_KEY,
                             ConnectorKeyProto.KeyType.GCM_CLIENT_EMAIL, ConnectorKeyProto.KeyType.PAGER_DUTY_API_KEY,
                             ConnectorKeyProto.KeyType.POSTGRES_PASSWORD, ConnectorKeyProto.KeyType.POSTGRES_USER,
                             ConnectorKeyProto.KeyType.GRAFANA_API_KEY,
                             ConnectorKeyProto.KeyType.OPS_GENIE_API_KEY,
                             ConnectorKeyProto.KeyType.OPEN_AI_API_KEY,
                             ConnectorKeyProto.KeyType.REMOTE_SERVER_PASSWORD,
                             ConnectorKeyProto.KeyType.REMOTE_SERVER_PEM,
                             ConnectorKeyProto.KeyType.GRAFANA_HOST,
                             ConnectorKeyProto.KeyType.OPS_GENIE_API_KEY,
                             ConnectorKeyProto.KeyType.EKS_ROLE_ARN,
                             ConnectorKeyProto.KeyType.POSTGRES_HOST,
                             ConnectorKeyProto.KeyType.CLICKHOUSE_HOST,
                             ConnectorKeyProto.KeyType.SQL_DATABASE_CONNECTION_STRING_URI,
                             ConnectorKeyProto.KeyType.SLACK_APP_ID]:
            key_value = '*********' + self.key[-4:]
        return ConnectorKeyProto(key_type=self.key_type,
                                 key=StringValue(value=key_value),
                                 is_active=BoolValue(value=self.is_active),
                                 connector_id=UInt64Value(value=self.connector_id),
                                 created_at=int(self.created_at.replace(tzinfo=timezone.utc).timestamp()),
                                 updated_at=int(self.updated_at.replace(tzinfo=timezone.utc).timestamp()),
                                 display_name=StringValue(
                                     value=integrations_connector_key_display_name_map.get(self.key_type, '')))

    @property
    def unmasked_proto(self):
        return ConnectorKeyProto(key_type=self.key_type,
                                 key=StringValue(value=self.key),
                                 is_active=BoolValue(value=self.is_active),
                                 connector_id=UInt64Value(value=self.connector_id),
                                 created_at=int(self.created_at.replace(tzinfo=timezone.utc).timestamp()),
                                 updated_at=int(self.updated_at.replace(tzinfo=timezone.utc).timestamp()),
                                 display_name=StringValue(
                                     value=integrations_connector_key_display_name_map.get(self.key_type, '')))


class ConnectorMetadataModelStore(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    connector = models.ForeignKey(Connector, on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    connector_type = models.IntegerField(choices=generate_choices(Source), default=Source.UNKNOWN,
                                         db_index=True)
    model_type = models.IntegerField(choices=generate_choices(SourceModelType), default=SourceModelType.UNKNOWN_MT,
                                     db_index=True)

    model_uid = models.TextField(db_index=True)

    metadata = models.JSONField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        unique_together = [['account', 'connector', 'connector_type', 'model_type', 'model_uid']]

    def __str__(self):
        return f'{self.account}:{self.connector_type}:{self.model_type}:{self.model_uid}'


class SlackConnectorAlertType(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_index=True)
    connector = models.ForeignKey(Connector, on_delete=models.CASCADE)
    channel_id = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    alert_type = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        unique_together = [['account', 'connector', 'channel_id', 'alert_type']]


class SlackConnectorDataReceived(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_index=True)
    connector = models.ForeignKey(Connector, on_delete=models.CASCADE)
    slack_channel_metadata_model = models.ForeignKey(ConnectorMetadataModelStore, on_delete=models.CASCADE,
                                                     db_index=True, null=True)
    channel_id = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    data = models.JSONField(null=True, blank=True)

    db_alert_type = models.ForeignKey(SlackConnectorAlertType, on_delete=models.CASCADE, null=True, blank=True,
                                      db_index=True)
    alert_type = models.CharField(max_length=255, null=True, blank=True, db_index=True)

    tags = models.JSONField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    data_timestamp = models.DateTimeField(blank=True, null=True, db_index=True)
    received_at = models.DateTimeField(auto_now_add=True, db_index=True)


class ConnectorPeriodicRunMetadata(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_index=True)
    connector = models.ForeignKey(Connector, on_delete=models.CASCADE)
    metadata = models.JSONField()
    task_run_id = models.CharField(max_length=255)
    status = models.IntegerField(null=True, blank=True,
                                 choices=generate_choices(PeriodicRunStatus.StatusType))
    started_at = models.DateTimeField(blank=True, null=True, db_index=True)
    finished_at = models.DateTimeField(blank=True, null=True, db_index=True)


class Site(models.Model):
    domain = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    protocol = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, **kwargs):
        if self.domain:
            django_site, _ = DjangoSite.objects.get_or_create(id=1)
            django_site.domain = self.domain
            django_site.name = self.name
            django_site.save()
        super().save(**kwargs)
