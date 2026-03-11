// src/api/auth.api.js

import api from "./client";

/**
 * Register new organization + owner
 */
export function register(data) {
  return api.post("/auth/register/", data);
}

/**
 * Login
 */
export function login(data) {
  return api.post("/auth/login/", data);
}

/**
 * Fetch current user
 */
export async function fetchMe() {
  const res = await api.get("/auth/me/");
  return res.data;
}
