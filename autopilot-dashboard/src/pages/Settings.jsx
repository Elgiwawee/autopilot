// src/pages/Settings.jsx

import { useEffect, useState } from "react";
import AppLayout from "../../components/layout/AppLayout";

export default function AutopilotSettingsPage() {
  const [settings, setSettings] = useState([]);

  useEffect(() => {
    fetch("/api/v1/autopilot-settings/", {
      headers: { Authorization: `Bearer ${localStorage.token}` },
    })
      .then(res => res.json())
      .then(setSettings);
  }, []);

  function updateSetting(s, field, value) {
    fetch("/api/v1/autopilot-settings/", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${localStorage.token}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        cloud_account: s.cloud_account,
        mode: field === "mode" ? value : s.mode,
        max_risk_allowed: field === "risk" ? value : s.max_risk_allowed,
      }),
    });
  }

  return (
    <AppLayout title="Autopilot Settings">
      {settings.map(s => (
        <div
          key={s.cloud_account}
          className="card p-6 mb-4 flex justify-between items-center"
        >
          <div>
            <div className="font-semibold">
              Cloud Account: {s.cloud_account}
            </div>
            <div className="text-sm text-muted">
              Risk Threshold: {s.max_risk_allowed}
            </div>
          </div>

          <div className="flex gap-4">
            <select
              defaultValue={s.mode}
              onChange={e =>
                updateSetting(s, "mode", e.target.value)
              }
              className="select"
            >
              <option value="safe">Safe</option>
              <option value="balanced">Balanced</option>
              <option value="aggressive">Aggressive</option>
            </select>

            <input
              type="number"
              defaultValue={s.max_risk_allowed}
              onBlur={e =>
                updateSetting(s, "risk", e.target.value)
              }
              className="input w-24"
            />
          </div>
        </div>
      ))}
    </AppLayout>
  );
}
