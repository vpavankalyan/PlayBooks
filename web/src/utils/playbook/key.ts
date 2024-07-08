export const Key = {
  METHOD: "method",
  URL: "url",
  HEADERS: "headers",
  PAYLOAD: "payload",
  TIMEOUT: "timeout",
  NAMESPACE: "namespace",
  REGION: "region",
  DIMENSION_NAME: "dimensions.0.name",
  DIMENSION_VALUE: "dimensions.0.value",
  METRIC_NAME: "metric_name",
} as const;

export type KeyType = (typeof Key)[keyof typeof Key];
