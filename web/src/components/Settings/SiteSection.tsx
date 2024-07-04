import React, { useState, useEffect } from "react";
import SettingsTitle from "./SettingsTitle.tsx";
import CustomButton from "../common/CustomButton/index.tsx";

function SiteSection() {
  const [value, setValue] = useState("https://example.com");
  const [error, setError] = useState("");

  const validate = () => {
    let errorString = "";
    if (!value || !value.trim()) {
      errorString = "Site URL is required";
    }

    if (errorString) {
      setError(errorString);
      return false;
    }

    return true;
  };

  const removeError = () => {
    if (!validate()) return;
    setError("");
  };

  const handleUpdate = () => {
    if (!validate()) return;
  };

  useEffect(() => {
    removeError();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [value]);

  return (
    <section className="border-b pb-4 mb-4">
      <SettingsTitle title="Site URL" />
      <div className="mt-2 flex items-baseline gap-2">
        <div className="flex flex-col">
          <input
            className="border p-1 text-sm outline-none rounded w-64"
            value={value}
            type="url"
            placeholder="Your Site URL"
            onChange={(e) => setValue(e.target.value)}
          />
          {error && <p className="text-red-500 text-xs">{error}</p>}
        </div>
        <CustomButton onClick={handleUpdate}>Update</CustomButton>
      </div>
    </section>
  );
}

export default SiteSection;