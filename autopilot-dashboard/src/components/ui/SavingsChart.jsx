// src/components/ui/SavingsChart.jsx

import {
  BarChart,
  Bar,
  XAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const data = [
  { name: "GPU Rightsizing", value: 8200 },
  { name: "Spot Usage", value: 6100 },
  { name: "Idle Reduction", value: 4100 },
];

export default function SavingsChart() {
  return (
    <div className="bg-panel border border-border rounded-lg p-6 h-72">
      <div className="font-semibold mb-4">Savings Breakdown</div>
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data}>
          <XAxis dataKey="name" stroke="#9CA3AF" />
          <Tooltip />
          <Bar dataKey="value" fill="#5B8CFF" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
