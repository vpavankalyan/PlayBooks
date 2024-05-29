export const extractPostgresTasks = (step: any) => {
  let stepSource = "POSTGRES";
  let modelType = "POSTGRES_QUERY";
  let selected = "POSTGRES Sql Query";
  const tasks = step.tasks;
  const postgresTask = tasks[0].data_fetch_task?.postgres_data_fetch_task;

  const stepData = {
    source: stepSource,
    selectedSource: selected,
    connector_type: stepSource,
    model_type: modelType,
    modelType,
    dbQuery: postgresTask?.query,
  };

  return stepData;
};
