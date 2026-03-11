import api from "./client";

export const getGlobalSafety = async () => {
  const res = await api.get("/global-safety/");
  return res.data;
};

export const getAutopilotSettings = async () => {
  const res = await api.get("/autopilot-settings/");
  return res.data;
};
