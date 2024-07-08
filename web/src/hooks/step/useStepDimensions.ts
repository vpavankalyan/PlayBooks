import { useEffect, useRef } from "react";
import updateStepById from "../../utils/playbook/step/updateStepById.ts";

function useStepDimensions(stepId: string) {
  const stepRef = useRef<HTMLDivElement>(null);

  const setDimensions = () => {
    const height = (stepRef.current?.clientHeight ?? 0) + 200;
    const width = (stepRef.current?.clientWidth ?? 0) + 20;
    updateStepById("ui_requirement.width", width, stepId);
    updateStepById("ui_requirement.height", height, stepId);
  };

  useEffect(() => {
    if (stepRef.current) {
      setDimensions();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [stepRef.current?.clientHeight, stepRef.current?.clientWidth]);

  return stepRef;
}

export default useStepDimensions;