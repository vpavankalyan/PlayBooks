import React, { useEffect, useState } from 'react';
import { CircularProgress } from '@mui/material';
import { useGetConnectorTypesQuery } from '../../../store/features/playbook/api/index.ts';
import { integrationSentenceMap, integrations } from '../../../utils/integrationGroupList.ts';
import IntegrationOption from './IntegrationOption.jsx';

function IntegrationsList({ setIsOpen }) {
  const { data: connectorData, isFetching: connectorLoading } = useGetConnectorTypesQuery();
  const [items, setItems] = useState(connectorData || []);

  useEffect(() => {
    setItems(connectorData || []);
  }, [connectorData]);

  const search = e => {
    const query = e.target.value.toLowerCase();
    const filteredItems = query
      ? connectorData?.filter(
          item =>
            item.connector_type.toLowerCase().includes(query) ||
            item.display_name.toLowerCase().includes(query)
        )
      : connectorData;
    setItems(filteredItems || []);
  };

  const integrationGroups = integrations.map(group => ({
    ...group,
    options: group.options
      .map(modelType => {
        const item = items.find(item => item.model_type === modelType);
        return item ? { ...item, label: integrationSentenceMap[modelType] } : null;
      })
      .filter(option => option !== null)
  }));

  return (
    <div>
      <h2 className="mt-4 font-bold text-sm">Add Data</h2>
      <input
        type="search"
        className="w-full p-2 border-[1px] border-gray-200 rounded text-sm my-2 outline-violet-500"
        placeholder="Search for integrations..."
        onChange={search}
      />
      {connectorLoading && (
        <div className="flex items-center gap-4 text-sm">
          <CircularProgress color="primary" size={20} />
          Looking for integrations...
        </div>
      )}
      <div className="flex flex-col gap-4">
        {integrationGroups.map(group => (
          <div key={group.id}>
            <p className="font-bold text-sm mb-1">{group.label}</p>
            <div className="flex flex-col gap-2">
              {group.options.length === 0 && <p className="text-xs">No integrations yet.</p>}
              {group.options.map(option => (
                <IntegrationOption option={option} setIsOpen={setIsOpen} />
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default IntegrationsList;
