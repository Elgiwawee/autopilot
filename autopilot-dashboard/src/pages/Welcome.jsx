// src/pages/Welcome.jsx

import { Link } from "react-router-dom"

export default function Welcome() {
  return (
    <div className="min-h-screen flex flex-col">
      <nav className="flex justify-between items-center px-8 py-5 border-b border-border">
        <h1 className="text-xl font-semibold text-primary">Cloud Autopilot</h1>
        <div className="space-x-4">
          <Link to="/login" className="text-muted hover:text-white">Login</Link>
          <Link
            to="/register"
            className="bg-primary text-black px-4 py-2 rounded-lg font-medium"
          >
            Get Started
          </Link>
        </div>
      </nav>

      <main className="flex-1 flex items-center justify-center text-center px-6">
        <div className="max-w-2xl">
          <h2 className="text-4xl font-bold leading-tight">
            Autonomous Cloud Optimization.
            <br /> Real Savings. Zero Guesswork.
          </h2>
          <p className="mt-6 text-muted text-lg">
            AI-driven cloud cost reduction with full auditability,
            safety controls, and executive-ready reporting.
          </p>

          <div className="mt-8 flex justify-center gap-4">
            <Link
              to="/register"
              className="bg-primary text-black px-6 py-3 rounded-lg font-semibold"
            >
              Start Free
            </Link>
            <Link
              to="/login"
              className="border border-border px-6 py-3 rounded-lg"
            >
              Sign In
            </Link>
          </div>
        </div>
      </main>
    </div>
  )
}
