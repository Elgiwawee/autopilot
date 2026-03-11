// src/components/ui/Card.jsx

export default function Card({ title, children }) {
  return (
    <div className="bg-white dark:bg-zinc-900 rounded-xl shadow p-4">
      {title && <h3 className="font-medium mb-3">{title}</h3>}
      {children}
    </div>
  );
}
