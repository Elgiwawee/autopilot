// src/components/ui/Badge.jsx

const variants = {
  green: "bg-green-100 text-green-700",
  gray: "bg-gray-100 text-gray-700"
};

export default function Badge({ children, variant = "gray" }) {
  return (
    <span className={`px-2 py-1 rounded text-xs ${variants[variant]}`}>
      {children}
    </span>
  );
}
