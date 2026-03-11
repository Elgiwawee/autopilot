import api from "./client";

export const getBillingSummary = async () => {
  const res = await api.get("/billing/summary/");
  return res.data;
};

export const getInvoices = async () => {
  const res = await api.get("/billing/invoices/");
  return res.data;
};

export const exportBilling = (invoiceId, format) =>
  api.get(
    `/billing/invoices/${invoiceId}/export/${format}/`,
    { responseType: "blob" }
  );
