// src/api/overview.api.js

import api from "./client";

export async function fetchOverview(params = {}) {
  const res = await api.get("/overview/", { params });
  return res.data;
}
