// src/pages/Register.jsx

import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { register } from "../api/auth.api";

export default function Register() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    organization_name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const [error, setError] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    setError(null);

    if (form.password !== form.confirmPassword) {
      setError("Passwords do not match");
      return;
    }

    try {
      await register({
        email: form.email,
        password: form.password,
        organization_name: form.organization_name,
      });

      navigate("/login");
    } catch (err) {
      console.error("REGISTER ERROR:", err.response?.data || err);
      setError(JSON.stringify(err.response?.data || "Registration failed"));
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center">
      <form
        onSubmit={handleSubmit}
        className="bg-panel border border-border p-8 rounded-lg w-96"
      >
        <h1 className="text-2xl font-semibold mb-6">
          Create Organization
        </h1>

        {error && (
          <div className="mb-4 text-danger text-sm">
            {error}
          </div>
        )}

        <input
          className="input mb-4 w-full"
          placeholder="Organization Name"
          value={form.organization_name}
          onChange={e =>
            setForm({ ...form, organization_name: e.target.value })
          }
        />

        <input
          className="input mb-4 w-full"
          placeholder="Email"
          value={form.email}
          onChange={e =>
            setForm({ ...form, email: e.target.value })
          }
        />

        <input
          className="input mb-4 w-full"
          type="password"
          placeholder="Password"
          value={form.password}
          onChange={e =>
            setForm({ ...form, password: e.target.value })
          }
        />

        <input
          className="input mb-6 w-full"
          type="password"
          placeholder="Confirm Password"
          value={form.confirmPassword}
          onChange={e =>
            setForm({ ...form, confirmPassword: e.target.value })
          }
        />

        <button className="w-full bg-primary py-2 rounded-lg font-medium">
          Register
        </button>
      </form>
    </div>
  );
}
