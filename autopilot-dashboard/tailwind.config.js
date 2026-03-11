// tailwind.config.js

export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        bg: "#0B1220",
        panel: "#111827",
        border: "#1F2937",
        primary: "#38BDF8",
        success: "#22C55E",
        warning: "#F59E0B",
        danger: "#EF4444",
        muted: "#9CA3AF",
      },
    },
  },
  plugins: [],
}
