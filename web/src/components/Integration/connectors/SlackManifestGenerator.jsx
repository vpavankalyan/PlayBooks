import { ContentCopy, InfoOutlined } from "@mui/icons-material";
import React, { useState } from "react";
import { HandleInputRender } from "../../common/HandleInputRender/HandleInputRender";
import { useDispatch, useSelector } from "react-redux";
import { connectorSelector } from "../../../store/features/integrations/integrationsSlice.ts";
import { useGenerateManifestMutation } from "../../../store/features/integrations/api/generateManifestApi.ts";
import { showSnackbar } from "../../../store/features/snackbar/snackbarSlice.ts";

function SlackManifestGenerator() {
  const [host, setHost] = useState("");
  const dispatch = useDispatch();
  const [triggerManifest] = useGenerateManifestMutation();
  const currentConnector = useSelector(connectorSelector);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!host) {
      dispatch(showSnackbar("Please enter a host name"));
      return;
    }

    triggerManifest(host);
  };

  return (
    <main className="p-2 my-2 rounded bg-white border mr-3">
      <form
        onSubmit={handleSubmit}
        className="flex my-2 items-end gap-2 flex-wrap">
        <HandleInputRender
          option={{
            type: "string",
            label: "Host Name",
            value: host,
            handleChange: setHost,
          }}
        />
        <button className="p-1 text-violet-500 hover:text-white hover:bg-violet-500 border border-violet-500 text-xs rounded cursor-pointer transition-all">
          Get Manifest
        </button>
      </form>

      {currentConnector.manifest && (
        <div className="my-2 lg:max-w-xl">
          <div className="w-full flex justify-end">
            <button className="border my-2 bg-white rounded p-1 text-xs font-bold flex gap-1 items-center cursor-pointer hover:border-violet-500 hover:text-violet-500 transition-all">
              <ContentCopy fontSize="small" />
              Copy Code
            </button>
          </div>
          <div className="border bg-gray-100 h-64 relative overflow-scroll p-2 text-gray-500">
            {currentConnector.manifest}
          </div>
        </div>
      )}

      <hr />

      <div className="bg-gray-100 rounded my-2 text-sm p-2 text-violet-500 flex items-center gap-2 font-semibold">
        <InfoOutlined /> After the slack app is created, share the following
      </div>
    </main>
  );
}

export default SlackManifestGenerator;
