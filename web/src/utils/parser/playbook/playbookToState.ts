import { injectTimeRangeIdFromSeconds } from "../../../components/Playbooks/task/taskConfiguration/comparison/utils";
import { commonKeySelector } from "../../../store/features/common/commonSlice.ts";
import { store } from "../../../store/index.ts";
import { Playbook, Step, Task } from "../../../types/index.ts";
import { v4 as uuidv4 } from "uuid";
import { exampleInputTransformer } from "../../common/transformerDefaults.ts";
import { relationToState } from "./relationToState.ts";

function playbookToState(playbook: Playbook): Playbook {
  const { supportedTaskTypes } = commonKeySelector(store.getState());
  const tasks: Task[] = [];
  const steps = playbook?.steps?.map((e: Step, i: number) => ({
    ...e,
    ui_requirement: {
      stepIndex: i === 0 ? 0 : undefined,
      isOpen: false,
      showError: false,
    },
  }));
  steps.forEach((step: Step) => {
    const stepTasks: Task[] = (step.tasks as Task[])
      .map((e) => {
        const supportedType = supportedTaskTypes?.find(
          (t: any) =>
            t.source === e.source &&
            t.task_type === e[e.source.toLowerCase()]?.type,
        );
        if (!supportedType) return undefined;
        return {
          ...e,
          reference_id: uuidv4(),
          transformer_code: e.transformer_code ?? "",
          execution_configuration: {
            ...e.execution_configuration,
            timeseries_offsets: [
              (
                parseInt(
                  e.execution_configuration?.timeseries_offsets?.[0] ?? "0",
                  10,
                ) / 3600
              ).toString(),
            ],
          },
          ui_requirement: {
            stepId: step.id,
            resultType: supportedType.result_type,
            isOpen: false,
            model_type: supportedType.supported_model_types?.[0]?.model_type,
            timeseries_offset_id: injectTimeRangeIdFromSeconds(
              e?.execution_configuration?.timeseries_offsets?.[0] ?? "",
            ),
            use_comparison:
              e?.execution_configuration?.timeseries_offsets &&
              (e?.execution_configuration?.timeseries_offsets?.length ?? 0) > 0,
            example_input: exampleInputTransformer,
          },
        };
      })
      .filter((result) => result !== undefined);
    step.reference_id = uuidv4();
    tasks.push(...stepTasks);
  });
  relationToState(playbook, tasks, steps);
  return {
    ...playbook,
    steps,
    ui_requirement: {
      tasks,
      isExisting: true,
    },
  };
}

export default playbookToState;
