import { store } from "../store/index.ts";
import { stepsSelector } from "../store/features/playbook/playbookSlice.ts";
import { showSnackbar } from "../store/features/snackbar/snackbarSlice.ts";
import { updateCardByIndex } from "./execution/updateCardByIndex.ts";

export default function handlePlaybookSavingValidations() {
  const steps = stepsSelector(store.getState());
  const dispatch = store.dispatch;
  let error = "";

  if (steps?.length === 0) {
    error = "You cannot save a playbook with no steps";
  }

  steps?.forEach((step, index) => {
    if (Object.keys(step.errors ?? {}).length > 0) {
      updateCardByIndex("showError", true, index);
      error = "Please fix the errors in the playbook";
    }
  });

  if (error) {
    dispatch(showSnackbar(error));
  }

  return error;
}
