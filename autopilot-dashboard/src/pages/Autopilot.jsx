import { useEffect, useState } from "react";
import {
  getAutopilotStatus,
  updateAutopilotMode,
  runAutopilotNow
} from "../api/autopilot.api";

import Card from "../components/ui/Card";
import Spinner from "../components/ui/Spinner";

const MODES = [
  "OFF",
  "RECOMMEND",
  "AUTO_SAFE",
  "AUTO_AGGRESSIVE"
];

export default function Autopilot() {
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getAutopilotStatus()
      .then(setStatus)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <Spinner />;

  const autoDisabled = !status.autopilot_enabled;

  const changeMode = (accountId, mode) => {
    if (autoDisabled) return;

    updateAutopilotMode(accountId, mode)
      .then(() => getAutopilotStatus().then(setStatus));
  };

  return (
    <div className="space-y-6">

      {!status.autopilot_enabled && (
        <div className="bg-red-100 text-red-700 p-4 rounded">
          Autopilot is globally disabled
        </div>
      )}

      {status.accounts.map(account => (
        <Card key={account.cloud_account_id}
              title={`Cloud Account ${account.cloud_account_id}`}>
          
          <p className="mb-2">
            Current Mode: <strong>{account.mode}</strong>
          </p>

          <div className="flex gap-2 flex-wrap">
            {MODES.map(m => (
              <button
                key={m}
                disabled={autoDisabled}
                onClick={() =>
                  changeMode(account.cloud_account_id, m)
                }
                className={`btn ${
                  account.mode === m ? "btn-primary" : ""
                }`}
              >
                {m}
              </button>
            ))}
          </div>

        </Card>
      ))}

      <Card title="Manual Execution">
        <button
          disabled={autoDisabled}
          onClick={runAutopilotNow}
          className="btn btn-danger"
        >
          Run Now
        </button>
      </Card>
    </div>
  );
}