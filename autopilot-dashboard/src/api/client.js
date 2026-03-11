// src/api/client.js

import axios from "axios";


const api = axios.create({
  baseURL: "/api/v1",
});

api.interceptors.request.use(config => {
  const token = localStorage.getItem("token");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  const org = JSON.parse(localStorage.getItem("active_org"));

  if (org?.id) {
    config.headers["X-Organization-ID"] = org.id;
  }

  return config;
});

export default api;