import api from "./client";

export const getPolicies = async () => {
  const res = await api.get("/policies");
  return res.data;
};

export const createPolicy = async (payload) => {
  const res = await api.post("/policies", payload);
  return res.data;
};

export const togglePolicy = async (id, enabled) => {
  const res = await api.patch(`/policies/${id}`, { enabled });
  return res.data;
};
