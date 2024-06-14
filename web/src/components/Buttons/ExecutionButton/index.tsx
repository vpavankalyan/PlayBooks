import React from "react";
import CustomButton from "../../common/CustomButton/index.tsx";
import { PlayArrowRounded, StopCircleRounded } from "@mui/icons-material";
import { CircularProgress } from "@mui/material";
import { useStartExecutionMutation } from "../../../store/features/playbook/api/index.ts";
import { useNavigate, useSearchParams } from "react-router-dom";
import {
  playbookSelector,
  setPlaybookKey,
} from "../../../store/features/playbook/playbookSlice.ts";
import { useDispatch, useSelector } from "react-redux";
import { executeStep } from "../../../utils/execution/executeStep.ts";
import useCurrentStep from "../../../hooks/useCurrentStep.ts";

function ExecutionButton() {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const currentPlaybook = useSelector(playbookSelector);
  const [step] = useCurrentStep(0);
  const [searchParams, setSearchParams] = useSearchParams();
  const executionId = searchParams.get("executionId");
  const [triggerStartExecution, { isLoading: executionLoading }] =
    useStartExecutionMutation();

  const handleStartExecution = async () => {
    if (executionId) return;
    const response = await triggerStartExecution(currentPlaybook.id);
    if ("data" in response) {
      const { data } = response;
      setSearchParams({ executionId: data.playbook_run_id });
      const id = data.playbook_run_id;
      dispatch(setPlaybookKey({ key: "executionId", value: id }));
      await executeStep(step, 0);
    }
  };

  const handleStopExecution = () => {
    if (!executionId) return;
    navigate(`/playbooks/${currentPlaybook.id}`, { replace: true });
  };

  return (
    <>
      {executionLoading && (
        <CircularProgress
          style={{
            textAlign: "center",
          }}
          size={20}
        />
      )}
      {executionId ? (
        <CustomButton onClick={handleStopExecution}>
          <StopCircleRounded />
          <span>Stop Execution</span>
        </CustomButton>
      ) : (
        <CustomButton onClick={handleStartExecution}>
          <PlayArrowRounded />
          <span>Start Execution</span>
        </CustomButton>
      )}
    </>
  );
}

export default ExecutionButton;