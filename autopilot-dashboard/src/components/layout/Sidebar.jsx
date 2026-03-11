// src/components/layout/Sidebar.jsx

import {
  LayoutDashboard,
  Cpu,
  Server,
  DollarSign,
  Settings,
} from "lucide-react";
import { NavLink } from "react-router-dom";

const links = [
  { to: "/overview", icon: LayoutDashboard, label: "Overview" },
  { to: "/infra", icon: Server, label: "Infrastructure" },
  { to: "/gpus", icon: Cpu, label: "GPUs" },
  { to: "/savings", icon: DollarSign, label: "Savings" },
  { to: "/settings/autopilot", icon: Settings, label: "Settings" },
];

export default function Sidebar() {
  return (
    <aside className="w-64 bg-panel border-r border-border flex flex-col">
      
      <div className="p-6 text-xl font-semibold text-primary">
        Cloud Autopilot
      </div>

      <nav className="px-4 space-y-2 flex-1">
        {links.map(({ to, icon: Icon, label }) => (
          <NavLink
            key={to}
            to={to}
            className={({ isActive }) =>
              `flex items-center gap-3 px-4 py-3 rounded-lg text-sm transition-all ${
                isActive
                  ? "bg-primary/10 text-primary"
                  : "text-muted hover:bg-border"
              }`
            }
          >
            <Icon size={18} />
            {label}
          </NavLink>
        ))}
      </nav>

    </aside>
  );
}