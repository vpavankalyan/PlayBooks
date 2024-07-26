import useIsPrefetched from "../../hooks/useIsPrefetched.ts";
import { useDispatch, useSelector } from "react-redux";
import {
  currentPlaybookSelector,
  playbookSelector,
  setCurrentPlaybookKey,
} from "../../store/features/playbook/playbookSlice.ts";

function PlaybookDescription() {
  const dispatch = useDispatch();
  const { isOnPlaybookPage } = useSelector(playbookSelector);
  const currentPlaybook = useSelector(currentPlaybookSelector);
  const isPrefetched = useIsPrefetched();

  if (!isOnPlaybookPage) return;
  if (isPrefetched && !currentPlaybook?.description) return;

  const handleDescription = (e) => {
    const value = e.target.value;
    dispatch(setCurrentPlaybookKey({ key: "description", value: value }));
  };

  return (
    <input
      className="font-normal text-xs p-1 w-[350px] rounded border border-transparent hover:border-gray-300 transition-all"
      placeholder={
        isPrefetched ? "Playbook Description goes here" : "+ Add Description..."
      }
      value={currentPlaybook?.description}
      onChange={handleDescription}
      disabled={isPrefetched !== "" ?? false}
    />
  );
}

export default PlaybookDescription;
