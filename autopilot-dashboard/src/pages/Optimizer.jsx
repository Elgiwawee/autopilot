// src/pages/Optimizer.jsx
import AppLayout from "../components/layout/AppLayout";

export default function Optimizer() {
  return (
    <AppLayout>
      <div className="space-y-4">
        <div className="bg-panel border border-border rounded-lg p-5">
          <div className="font-semibold">Active Rules</div>
          <ul className="mt-3 text-sm text-muted space-y-2">
            <li>✔ Scale down idle GPUs</li>
            <li>✔ Prefer spot instances</li>
            <li>✔ Pod consolidation</li>
          </ul>
        </div>

        <div className="bg-panel border border-border rounded-lg p-5">
          <div className="font-semibold">Planned Actions</div>
          <ul className="mt-3 text-sm">
            <li>→ Terminate node-7</li>
            <li>→ Move job-221 to spot</li>
          </ul>
        </div>
      </div>
    </AppLayout>
  );
}
