import { useEffect, useState } from "react";
import {
  fetchCloudAccounts,
  createCloudAccount,
  disableCloudAccount,
} from "../../api/cloudAccounts";

export default function CloudAccountsPage() {
  const [accounts, setAccounts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [submitting, setSubmitting] = useState(false);

  const [form, setForm] = useState({
    provider_code: "aws",
    account_identifier: "",
    role_arn: "",
    mode: "observe",
  });

  useEffect(() => {
    console.log("CloudAccountsPage mounted");
  }, []);

  useEffect(() => {
    loadAccounts();
  }, []);

  async function loadAccounts() {
    try {
      const res = await fetchCloudAccounts();
      console.log("API response:", res);
      setAccounts(res.results || []);
    } catch (err) {
      console.error("Failed to load cloud accounts", err);
      setAccounts([]);
    } finally {
      setLoading(false);
    }
  }

  async function handleCreate(e) {
    e.preventDefault();
    setSubmitting(true);

    try {
      const newAccount = await createCloudAccount(form);
      setAccounts(prev => [...prev, newAccount]);
      setShowModal(false);
      setForm({
        provider_code: "aws",
        account_identifier: "",
        role_arn: "",
        mode: "observe",
      });
    } catch (err) {
      console.error("Failed to create account", err);
    } finally {
      setSubmitting(false);
    }
  }

  async function handleDisable(id) {
    if (!window.confirm("Disable this cloud account?")) return;

    try {
      await disableCloudAccount(id);
      setAccounts(prev => prev.filter(acc => acc.id !== id));
    } catch (err) {
      console.error("Failed to disable account", err);
    }
  }

  return (
    <>
      {/* Action Bar */}
      <div className="flex justify-between items-center mb-6">
        <div className="text-sm text-muted">
          Manage connected cloud environments
        </div>

        <button
          onClick={() => setShowModal(true)}
          className="btn-primary"
        >
          + Connect Cloud Account
        </button>
      </div>

      {/* Loading */}
      {loading ? (
        <div className="text-muted">Loading cloud accounts…</div>
      ) : accounts.length === 0 ? (
        <div className="flex flex-col items-center justify-center py-20 text-center">
          <div className="text-4xl mb-4">☁️</div>

          <h2 className="text-lg font-semibold mb-2">
            No Cloud Accounts Connected
          </h2>

          <p className="text-muted text-sm mb-6 max-w-sm">
            Connect your first cloud account to start monitoring costs,
            optimization opportunities and savings.
          </p>

          <button
            onClick={() => setShowModal(true)}
            className="btn-primary"
          >
            + Connect Cloud Account
          </button>
        </div>
      ) : (
        <table className="w-full border-collapse">
          <thead className="text-muted text-sm border-b">
            <tr>
              <th className="text-left py-3">Provider</th>
              <th className="text-left py-3">Account ID</th>
              <th className="text-left py-3">Mode</th>
              <th className="text-left py-3">Status</th>
              <th className="text-left py-3">Connected</th>
              <th className="text-right py-3">Actions</th>
            </tr>
          </thead>

          <tbody>
            {accounts.map(acc => (
              <tr key={acc.id} className="border-b last:border-b-0">
                <td className="py-3 capitalize font-medium">
                  {acc.provider}
                </td>

                <td className="py-3 font-mono text-sm">
                  {acc.account_identifier}
                </td>

                <td className="py-3">
                  <span
                    className={`px-2 py-1 rounded text-xs font-medium ${
                      acc.mode === "autopilot"
                        ? "bg-success/10 text-success"
                        : acc.mode === "recommend"
                        ? "bg-warning/10 text-warning"
                        : "bg-muted/20 text-muted"
                    }`}
                  >
                    {acc.mode.toUpperCase()}
                  </span>
                </td>

                <td className="py-3">
                  <span className="text-success text-sm">
                    ● {acc.status}
                  </span>
                </td>

                <td className="py-3 text-sm text-muted">
                  {acc.created_at
                    ? new Date(acc.created_at).toLocaleDateString()
                    : "—"}
                </td>

                <td className="py-3 text-right">
                  <button
                    onClick={() => handleDisable(acc.id)}
                    className="text-danger text-sm hover:underline"
                  >
                    Disable
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {/* Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-black/40 flex items-center justify-center z-50">
          <div className="bg-card rounded-lg w-full max-w-md p-6">
            <h3 className="text-lg font-semibold mb-4">
              Connect Cloud Account
            </h3>

            <form onSubmit={handleCreate} className="space-y-4">
              <div>
                <label className="text-sm">Provider</label>
                <select
                  className="input"
                  value={form.provider_code}
                  onChange={e =>
                    setForm({ ...form, provider_code: e.target.value })
                  }
                >
                  <option value="aws">AWS</option>
                  <option value="azure">Azure</option>
                  <option value="gcp">GCP</option>
                  <option value="kubernetes">Kubernetes</option>
                </select>
              </div>

              <div>
                <label className="text-sm">Account Identifier</label>
                <input
                  className="input"
                  required
                  value={form.account_identifier}
                  onChange={e =>
                    setForm({
                      ...form,
                      account_identifier: e.target.value,
                    })
                  }
                />
              </div>

              <div>
                <label className="text-sm">Role ARN (optional)</label>
                <input
                  className="input"
                  value={form.role_arn}
                  onChange={e =>
                    setForm({
                      ...form,
                      role_arn: e.target.value,
                    })
                  }
                />
              </div>

              <div>
                <label className="text-sm">Mode</label>
                <select
                  className="input"
                  value={form.mode}
                  onChange={e =>
                    setForm({ ...form, mode: e.target.value })
                  }
                >
                  <option value="observe">Observe</option>
                  <option value="recommend">Recommend</option>
                  <option value="autopilot">Autopilot</option>
                </select>
              </div>

              <div className="flex justify-end gap-3 pt-4">
                <button
                  type="button"
                  onClick={() => setShowModal(false)}
                  className="btn-secondary"
                >
                  Cancel
                </button>

                <button
                  type="submit"
                  disabled={submitting}
                  className="btn-primary"
                >
                  {submitting ? "Connecting..." : "Connect"}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </>
  );
}