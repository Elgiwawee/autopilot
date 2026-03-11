// src/pages/settings/Sefety.jsx

import { useEffect, useState } from "react";
import { getGlobalSafety } from "../../api/safety.api";
import SafetyBanner from "../../components/safety/SafetyBanner";

export default function Safety() {
  const [safety, setSafety] = useState(null);

  useEffect(() => {
    getGlobalSafety().then(setSafety);
  }, []);

  if (!safety) return null;

  return (
    <div className="space-y-6">
      <SafetyBanner safety={safety} />

      <div className="bg-panel border border-border rounded-lg p-6">
        <h2 className="font-semibold mb-2">Global Autopilot Safety</h2>
        <p className="text-sm text-muted">
          This lock disables all automated actions across all cloud accounts.
        </p>

        <div className="mt-4 text-sm">
          Status:{" "}
          <span
            className={
              safety.autopilot_enabled
                ? "text-success"
                : "text-danger"
            }
          >
            {safety.autopilot_enabled ? "ENABLED" : "LOCKED"}
          </span>
        </div>
      </div>
    </div>
  );
}
