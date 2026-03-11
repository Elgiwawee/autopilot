import api from "./client";

export const getAuditLogs = async () => {
  const res = await api.get("/governance/audit-logs");
  return res.data;
};
