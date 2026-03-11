import { useEffect, useState } from "react";
import api from "../api/client"; // use your axios client

export default function AuditLogsPage() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    async function loadLogs() {
      try {
        const res = await api.get("/audit-logs/");
        setLogs(res.data.logs || []);
      } catch (err) {
        console.error("Failed to load audit logs", err);
      }
    }

    loadLogs();
  }, []);

  return (
    <>
      <h1 className="text-2xl font-semibold mb-6">
        Audit Logs
      </h1>

      <table className="w-full">
        <thead className="text-muted text-sm border-b">
          <tr>
            <th className="text-left py-3">Time</th>
            <th className="text-left py-3">Actor</th>
            <th className="text-left py-3">Action</th>
            <th className="text-left py-3">Resource</th>
            <th className="text-left py-3">Status</th>
          </tr>
        </thead>

        <tbody>
          {logs.map(log => (
            <tr key={log.timestamp} className="border-b">
              <td className="py-3">
                {new Date(log.timestamp).toLocaleString()}
              </td>

              <td className="py-3">
                {log.actor}
              </td>

              <td className="py-3">
                {log.action}
              </td>

              <td className="py-3">
                {log.resource_id}
              </td>

              <td
                className={`py-3 ${
                  log.status === "SUCCESS"
                    ? "text-success"
                    : "text-danger"
                }`}
              >
                {log.status}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
}