type CardsDataType = {
  url: string; // the logo url (from /public/integrations)
  enum: string; // enum from the backend
  desc?: string; // Description to show on the /data-sources/add page
  docs?: string; // Link to the documentation (to be shown while configuring)
};

export const cardsData: CardsDataType[] = [
  {
    url: "/integrations/sentry.png",
    enum: "SENTRY",
    desc: "Share alerts and error issues from Sentry",
  },
  {
    url: "/integrations/new-relic.png",
    enum: "NEW_RELIC",
    desc: "Connect metrics from New Relic",
    docs: "https://docs.drdroid.io/docs/new-relic-access",
  },
  {
    url: "/integrations/amazon-eks-icon.png",
    enum: "EKS",
    desc: "Connect EKS",
    docs: "https://docs.drdroid.io/docs/amazon-eks",
  },
  {
    url: "/integrations/slack-logo.svg",
    enum: "SLACK",
    desc: "Integrate Slack workspace",
    docs: "https://docs.drdroid.io/docs/slack-alerts",
  },
  {
    url: "/integrations/pagerduty_logo.png",
    enum: "PAGER_DUTY",
    desc: "Authorise Doctor Droid to read incidents from PagerDuty",
  },
  {
    url: "/integrations/elastic_search.png",
    enum: "ELASTIC_SEARCH",
    desc: "Setup Dr. Droid to periodically pull logs from your Elasic Search",
    docs: "https://docs.drdroid.io/docs/elk",
  },
  {
    url: "/integrations/aws-cloudwatch-logo.png",
    enum: "CLOUDWATCH",
    desc: "Connect metrics and logs from Cloudwatch",
    docs: "https://docs.drdroid.io/docs/aws-cloudwatch-access",
  },
  {
    url: "/integrations/datadoghq-icon.svg",
    enum: "DATADOG",
    desc: "Connect metrics from DataDog",
    docs: "https://docs.drdroid.io/docs/datadog-access",
  },
  {
    url: "/integrations/google-cloud-logo.png",
    enum: "GCM",
    desc: "Connect metrics and logs from Google Cloud",
  },
  {
    url: "/integrations/prometheus.webp",
    enum: "PROMETHEUS",
    desc: "Share metrics from your Prometheus instance",
  },
  {
    url: "/integrations/grafana_logo.png",
    enum: "GRAFANA",
    desc: "Share Data Sources, Dashboards & Metrics from Grafana",
    docs: "https://docs.drdroid.io/docs/custom-promql-query",
  },
  {
    url: "/integrations/clickhouse_logo.png",
    enum: "CLICKHOUSE",
    desc: "Connect Clickhouse tables",
    docs: "https://docs.drdroid.io/docs/clickhouse-database",
  },
  {
    url: "/integrations/postgresql_logo.png",
    enum: "POSTGRES",
    desc: "Connect Postgres tables",
    docs: "https://docs.drdroid.io/docs/postgresql-database",
  },
  {
    url: "/integrations/opsgenie-logo.png",
    enum: "OPS_GENIE",
    desc: "Authorise Doctor Droid to read incidents from OpsGenie",
  },
  {
    url: "/integrations/GitHub-Actions.svg",
    enum: "GITHUB_ACTIONS",
    desc: "Fetch Deployment Information data from Github Actions",
    docs: "https://docs.drdroid.io/docs/github-actions",
  },
  {
    url: "/integrations/sql-db-connection-logo.svg",
    enum: "SQL_DATABASE_CONNECTION",
    desc: "Connect tables from any SQL database",
    docs: "https://docs.drdroid.io/docs/sql-databases",
  },
  {
    url: "/integrations/code.png",
    enum: "API",
  },
  {
    url: "/integrations/open-ai-logo.png",
    enum: "OPEN_AI",
    desc: "Save OpenAI API key",
    docs: "https://docs.drdroid.io/docs/openai",
  },
  {
    url: "/integrations/markdown_logo.svg",
    enum: "DOCUMENTATION",
  },
  {
    url: "/integrations/remote_server_logo.png",
    enum: "BASH",
    desc: "Connect Remote Server",
    docs: "https://docs.drdroid.io/docs/bash-commands",
  },
  {
    url: "/integrations/mimir_logo.png",
    enum: "GRAFANA_MIMIR",
    desc: "Connect Metrics from Grafana Mimir",
    docs: "https://docs.drdroid.io/docs/mimir",
  },
  {
    url: "/integrations/azure_logo.png",
    enum: "AZURE",
    desc: "Connect Logs from Microsoft Azure Log Analytics",
    docs: "https://docs.drdroid.io/docs/azure-cloud-log-analytics",
  },
  {
    url: "/integrations/iframe_logo.png",
    enum: "IFRAME",
  },
  {
    url: "/integrations/gke_logo.svg",
    enum: "GKE",
    desc: "Connect GKE",
    docs: "https://docs.drdroid.io/docs/google-cloud-gke",
  },
  {
    url: "/integrations/ms_teams_logo.png",
    enum: "MS_TEAMS",
    desc: "Connect to MS Teams using Webhook",
    docs: "https://docs.drdroid.io/docs/ms-teams",
  },
  {
    url: "/integrations/grafana_loki_logo.svg",
    enum: "GRAFANA_LOKI",
    desc: "Connect to Grafana Loki",
    docs: "https://docs.drdroid.io/docs/grafana-loki-logs",
  },
  {
    url: "/integrations/kubernetes_logo.png",
    enum: "KUBERNETES",
    desc: "Connect to Kubernetes Cluster",
    docs: "https://docs.drdroid.io/docs/service-account-token",
  },
  {
    url: "/integrations/email_logo.png",
    enum: "SMTP",
    desc: "Connect to SMTP Server",
    docs: "https://docs.drdroid.io/docs/email",
  },
];
