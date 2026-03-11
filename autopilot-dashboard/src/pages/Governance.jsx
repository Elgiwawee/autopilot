// src/pages/Governance.jsx

import { useEffect, useState } from "react";
import { getAuditLogs } from "../api/governance.api";
import Card from "../components/ui/Card";
import Spinner from "../components/ui/Spinner";

export default function Governance() {
  const [logs, setLogs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getAuditLogs()
      .then(setLogs)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <Spinner />;

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold">Governance & Audit</h1>

      <Card title="Audit Logs">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b">
              <th>Time</th>
              <th>Actor</th>
              <th>Action</th>
              <th>Resource</th>
              <th>Result</th>
            </tr>
          </thead>
          <tbody>
            {logs.map(log => (
              <tr key={log.id} className="border-b">
                <td>{log.timestamp}</td>
                <td>{log.actor}</td>
                <td>{log.action}</td>
                <td>{log.resource}</td>
                <td>{log.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>
    </div>
  );
}
