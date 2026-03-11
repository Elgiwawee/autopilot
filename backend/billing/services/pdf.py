# billing/services/pdf.py

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from io import BytesIO


def export_invoice_pdf(invoice):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 50

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, f"Invoice INV-{invoice.id}")
    y -= 30

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Period: {invoice.period}")
    y -= 20
    c.drawString(50, y, f"Organization: {invoice.organization.name}")
    y -= 30

    # Table Header
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Gross Savings")
    c.drawString(200, y, "Platform Fee")
    y -= 15

    c.line(50, y, width - 50, y)
    y -= 20

    c.setFont("Helvetica", 11)

    total_savings = 0
    total_fee = 0

    for item in invoice.items.all():
        if y < 80:
            c.showPage()
            c.setFont("Helvetica", 11)
            y = height - 50

        c.drawString(50, y, f"${item.gross_savings:.2f}")
        c.drawString(200, y, f"${item.platform_fee:.2f}")

        total_savings += item.gross_savings
        total_fee += item.platform_fee
        y -= 20

    y -= 20
    c.line(50, y, width - 50, y)
    y -= 20

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Total Savings: ${total_savings:.2f}")
    y -= 20
    c.drawString(50, y, f"Total Platform Fee: ${total_fee:.2f}")

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer


def export_all_invoices_pdf(organization):
    from billing.models import Invoice

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, f"Billing Report - {organization.name}")
    y -= 40

    c.setFont("Helvetica", 11)

    invoices = Invoice.objects.filter(
        organization=organization
    ).order_by("-period")

    for inv in invoices:
        if y < 80:
            c.showPage()
            c.setFont("Helvetica", 11)
            y = height - 50

        c.drawString(
            50,
            y,
            f"INV-{inv.id} | {inv.period} | ${inv.amount_due} | {inv.status}"
        )
        y -= 20

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer
