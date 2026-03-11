// src/components/sefety/SefetyBanner.jsx

import { AlertTriangle, Lock } from "lucide-react";

export default function SafetyBanner({ safety }) {
  if (safety.autopilot_enabled) return null;

  return (
    <div className="flex items-center gap-3 p-4 mb-4 rounded-lg bg-red-900/20 border border-red-600">
      <Lock className="text-red-500" size={18} />
      <div>
        <p className="font-semibold text-red-400">
          Autopilot is globally disabled
        </p>
        <p className="text-sm text-red-300">
          No automated actions can run until this lock is removed.
        </p>
      </div>
    </div>
  );
}
