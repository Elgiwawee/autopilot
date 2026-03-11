// src/components/ui/CostTrendChart.jsx

import {
  LineChart,
  Line,
  XAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

export default function CostTrendChart({ data }) {
  return (
    <div className="bg-panel p-6 rounded-lg border border-border">
      <h3 className="font-medium mb-4">Cost Trend</h3>

      <ResponsiveContainer width="100%" height={260}>
        <LineChart data={data}>
          <XAxis dataKey="date" />
          <Tooltip />
          <Line
            dataKey="cost"
            stroke="#38BDF8"
            strokeWidth={2}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
