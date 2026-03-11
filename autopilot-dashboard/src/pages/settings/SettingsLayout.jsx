// src/pages/settings/SettingsLayout.jsx

import { NavLink, Outlet } from "react-router-dom";

const tabs = [
  { to: "cloud-accounts", label: "Cloud Accounts" },
  { to: "autopilot", label: "Autopilot" },
  { to: "policies", label: "Policies" },
  { to: "safety", label: "Safety Controls" },
  { to: "audit", label: "Audit Logs" },
  { to: "billing", label: "Billing" },
];

export default function SettingsLayout() {
  return (
    <div className="flex gap-8">
      {/* LEFT SETTINGS NAV */}
      <aside className="w-56 space-y-1">
        {tabs.map(t => (
          <NavLink
            key={t.to}
            to={t.to}
            className={({ isActive }) =>
              `block px-4 py-2 rounded-lg text-sm ${
                isActive
                  ? "bg-border text-white"
                  : "text-muted hover:bg-border"
              }`
            }
          >
            {t.label}
          </NavLink>
        ))}
      </aside>

      {/* CONTENT */}
      <div className="flex-1">
        <Outlet />
      </div>
    </div>
  );
}
