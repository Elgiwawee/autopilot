// src/pages/Policies.jsx

import { useEffect, useState } from "react";
import { getPolicies, togglePolicy } from "../api/policies.api";
import Card from "../components/ui/Card";
import Spinner from "../components/ui/Spinner";

export default function Policies() {
  const [policies, setPolicies] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getPolicies()
      .then(setPolicies)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <Spinner />;

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold">Policies</h1>

      <Card title="Optimization Policies">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b">
              <th>Name</th>
              <th>Description</th>
              <th>Action</th>
              <th>Enabled</th>
            </tr>
          </thead>
          <tbody>
            {policies.map(p => (
              <tr key={p.id} className="border-b">
                <td>{p.name}</td>
                <td>{p.description}</td>
                <td>{p.action}</td>
                <td>
                  <input
                    type="checkbox"
                    checked={p.enabled}
                    onChange={(e) =>
                      togglePolicy(p.id, e.target.checked)
                    }
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>
    </div>
  );
}
