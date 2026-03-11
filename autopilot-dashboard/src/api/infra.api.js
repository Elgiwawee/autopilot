// infra.api.js

import api from "./client";

export const getInfraOverview = async () => {
  const res = await api.get("/infra/overview");
  return res.data;
};

export const getCloudAccounts = async () => {
  const res = await api.get("/infra/cloud-accounts");
  return res.data;
};

export const getRegions = async () => {
  const res = await api.get("/infra/regions");
  return res.data;
};

export const getResources = async (params = {}) => {
  const res = await api.get("/infra/resources", { params });
  return res.data;
};
