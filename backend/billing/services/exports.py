# billing/services/exports.py

import csv
from io import StringIO


def export_invoice_csv(invoice):
    output = StringIO()
    writer = csv.writer(output)

    writer.writerow(["Invoice", f"INV-{invoice.id}"])
    writer.writerow(["Period", invoice.period])
    writer.writerow([])

    writer.writerow([
        "Gross Savings",
        "Platform Fee",
    ])

    total_savings = 0
    total_fee = 0

    for item in invoice.items.all():
        writer.writerow([
            item.gross_savings,
            item.platform_fee,
        ])
        total_savings += item.gross_savings
        total_fee += item.platform_fee

    writer.writerow([])
    writer.writerow(["Total Savings", total_savings])
    writer.writerow(["Total Platform Fee", total_fee])

    return output.getvalue()


def export_all_invoices_csv(organization):
    from billing.models import Invoice

    output = StringIO()
    writer = csv.writer(output)

    writer.writerow([
        "Invoice",
        "Period",
        "Amount",
        "Status",
    ])

    invoices = Invoice.objects.filter(
        organization=organization
    ).order_by("-period")

    for inv in invoices:
        writer.writerow([
            f"INV-{inv.id}",
            inv.period,
            inv.amount_due,
            inv.status,
        ])

    return output.getvalue()
