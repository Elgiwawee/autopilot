#control_plane/services/billing_service.py

from django.db.models import Avg
from billing.models import Invoice


def build_billing_overview(organization):
    invoices = (
        Invoice.objects
        .filter(organization=organization)
        .order_by("-period")
    )

    current = invoices.first()
    last = invoices[1] if invoices.count() > 1 else None

    average = invoices.aggregate(
        avg=Avg("platform_fee")
    )["avg"] or 0

    forecast = float(average) * 1.05  # simple 5% projection

    return {
        "current_month": current.platform_fee if current else 0,
        "last_month": last.platform_fee if last else 0,
        "average": round(float(average), 2),
        "forecast": round(float(forecast), 2),
    }
