import React from "react";
import CustomButton from "../../common/CustomButton/index.tsx";
import { Add } from "@mui/icons-material";
import useDrawerState from "../../../hooks/useDrawerState.ts";
import { DrawerTypes } from "../../../store/features/drawers/drawerTypes.ts";

const addDataId = DrawerTypes.ADD_DATA;

function AddTaskButton({ id }) {
  const { toggle: toggleAddData, addAdditionalData } =
    useDrawerState(addDataId);

  const handleNoAction = (
    e: React.MouseEvent<HTMLButtonElement, MouseEvent>,
  ) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleAddTask = (
    e: React.MouseEvent<HTMLButtonElement, MouseEvent>,
  ) => {
    handleNoAction(e);
    toggleAddData();
    addAdditionalData({ stepId: id });
  };

  return (
    <CustomButton onClick={handleAddTask}>
      <Add fontSize="small" />
      <p>Add Task</p>
    </CustomButton>
  );
}

export default AddTaskButton;