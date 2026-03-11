import api from "./client";

export const getGPUInventory = async (params = {}) => {
  const res = await api.get("/gpus", { params });
  return res.data;
};