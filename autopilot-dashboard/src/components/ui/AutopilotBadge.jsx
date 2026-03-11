// src/components/ui/AutopilotBadge.jsx

export default function AutopilotBadge({ autopilot }) {
  if (!autopilot) return null;

  const active = autopilot.effective_status === "ACTIVE";

  return (
    <span
      className={`px-3 py-1 rounded-full text-sm font-medium ${
        active
          ? "bg-success/20 text-success"
          : "bg-warning/20 text-warning"
      }`}
    >
      Autopilot {active ? "Active" : "Paused"}
    </span>
  );
}
