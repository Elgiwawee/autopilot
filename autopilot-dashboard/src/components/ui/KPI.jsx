// src/components/ui/KPI.jsx

export default function KPI({ title, value, subtitle }) {
  return (
    <div className="bg-panel border border-border rounded-lg p-6">
      <div className="text-sm text-muted">{title}</div>
      <div className="text-3xl font-semibold mt-2">
        {value}
      </div>
      {subtitle && (
        <div className="text-xs text-muted mt-1">
          {subtitle}
        </div>
      )}
    </div>
  );
}
