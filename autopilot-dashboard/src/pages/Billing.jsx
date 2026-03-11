// src/pages/Billing.jsx

import { useEffect, useState } from "react";
import {
  getBillingSummary,
  getInvoices,
  exportBilling
} from "../api/billing.api";

import Card from "../components/ui/Card";
import Spinner from "../components/ui/Spinner";

export default function Billing() {
  const [summary, setSummary] = useState(null);
  const [invoices, setInvoices] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([getBillingSummary(), getInvoices()])
      .then(([s, i]) => {
        setSummary(s);
        setInvoices(i);
      })
      .catch(err => {
        console.error("Billing load failed", err);
      })
      .finally(() => setLoading(false));
  }, []);

  const download = (fn, filename) => {
    fn().then(res => {
      const url = window.URL.createObjectURL(res.data);
      const a = document.createElement("a");
      a.href = url;
      a.download = filename;
      a.click();
    });
  };

  if (loading || !summary) return <Spinner />;
  
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold">Billing</h1>

      {/* Summary */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card title="This Month">${summary.current_month}</Card>
        <Card title="Last Month">${summary.last_month}</Card>
        <Card title="Avg Monthly">${summary.average}</Card>
        <Card title="Forecast">${summary.forecast}</Card>
      </div>

      {/* Invoices */}
      <Card title="Invoices">
        <table className="w-full text-sm">
          <thead>
            <tr className="border-b">
              <th>Invoice</th>
              <th>Month</th>
              <th>Amount</th>
              <th>Status</th>
              <th>Export</th>
            </tr>
          </thead>
            <tbody>
              {invoices.map(inv => (
                <tr key={inv.id} className="border-b">
                  <td>{inv.number}</td>
                  <td>{inv.month}</td>
                  <td>${inv.amount}</td>
                  <td>{inv.status}</td>

                  <td className="flex gap-2">
                    <button
                      onClick={() =>
                        download(
                          () => exportBilling(inv.id, "csv"),
                          `invoice-${inv.id}.csv`
                        )
                      }
                      className="btn"
                    >
                      CSV
                    </button>

                    <button
                      onClick={() =>
                        download(
                          () => exportBilling(inv.id, "pdf"),
                          `invoice-${inv.id}.pdf`
                        )
                      }
                      className="btn"
                    >
                      PDF
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
            {invoices.length === 0 && (
              <tr>
                <td colSpan="5" className="text-center py-6 text-gray-500">
                  No invoices yet.
                </td>
              </tr>
            )}
        </table>
      </Card>
    </div>
    );
}