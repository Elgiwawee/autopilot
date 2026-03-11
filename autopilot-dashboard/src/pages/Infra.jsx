// src/pages/Infra.jsx

import { useEffect, useState } from "react";
import {
  getInfraOverview,
  getCloudAccounts,
  getRegions,
  getResources
} from "../api/infra.api";
import Card from "../components/ui/Card";
import Spinner from "../components/ui/Spinner";

export default function Infra() {
  const [overview, setOverview] = useState(null);
  const [accounts, setAccounts] = useState([]);
  const [regions, setRegions] = useState([]);
  const [resources, setResources] = useState([]);
  
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    Promise.all([
      getInfraOverview(),
      getCloudAccounts(),
      getRegions(),
      getResources()
    ])
      .then(([o, a, r, res]) => {
        setOverview(o);
        setAccounts(a.results || a);
        setRegions(r.results || r);
        setResources(res.results || res);
      })
      .catch(err => {
        console.error(err);
        setError("Failed to load infrastructure data");
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <Spinner />;
  if (error) return <p className="text-red-500">{error}</p>;

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold">Infrastructure</h1>

      {/* Overview */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card title="Accounts">{overview.accounts}</Card>
        <Card title="Regions">{overview.regions}</Card>
        <Card title="Resources">{overview.resources}</Card>
        <Card title="Monthly Cost">${overview.monthly_cost}</Card>
      </div>

      {/* Cloud Accounts */}
      <Card title="Cloud Accounts">
        <table className="w-full text-sm">
          <thead>
            <tr className="text-left border-b">
              <th>Name</th>
              <th>Provider</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {accounts.map(acc => (
              <tr key={acc.id} className="border-b">
                <td>{acc.name}</td>
                <td>{acc.provider}</td>
                <td>{acc.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>

      {/* Resources */}
      <Card title="Resources">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b">
              <th>Name</th>
              <th>Type</th>
              <th>Region</th>
              <th>Cost</th>
            </tr>
          </thead>
          <tbody>
            {resources.map(r => (
              <tr key={r.id} className="border-b">
                <td>{r.name}</td>
                <td>{r.type}</td>
                <td>{r.region}</td>
                <td>${r.monthly_cost}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>
    </div>
  );
}
