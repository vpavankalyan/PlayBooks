import React from 'react';
import { cardsData } from '../../../utils/cardsData';
import { useDispatch } from 'react-redux';
import { createStepWithSource } from '../../../store/features/playbook/playbookSlice.ts';
import { integrationSentenceMap } from '../../../utils/integrationGroupList.ts';

function IntegrationOption({ option, setIsOpen }) {
  const dispatch = useDispatch();

  const handleClick = item => {
    dispatch(
      createStepWithSource({
        source: item.connector_type,
        modelType: item.model_type,
        key: integrationSentenceMap[item.model_type]
      })
    );
    setIsOpen(false);
  };

  return (
    <div
      className="flex items-center gap-2 p-2 bg-gray-50 rounded border-[1px]  hover:bg-gray-200 cursor-pointer transition-all"
      key={option.id}
      onClick={() => handleClick(option)}
    >
      <img
        className="w-10 h-10"
        src={cardsData.find(e => e.enum === option?.connector_type?.replace('_VPC', ''))?.url ?? ''}
        alt="logo"
      />
      {/* <div>
                    <p className="text-xs font-bold text-gray-500">{data.connector_type}</p>
                    <p className="font-semibold">{data.display_name}</p>
                  </div> */}
      <p className="text-sm">{option.label}</p>
    </div>
  );
}

export default IntegrationOption;
