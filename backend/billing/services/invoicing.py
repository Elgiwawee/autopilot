# billing/services/invoicing.py

from decimal import Decimal
from django.db import transaction
from django.db.models import Sum
from django.utils import timezone

from billing.models import (
    Invoice,
    InvoiceLineItem,
    SavingsLedger,
    RevenueShare,
)


@transaction.atomic
def generate_monthly_invoice(organization, period: str):
    """
    Generates a monthly invoice for an organization.
    Period format: YYYY-MM
    """

    if Invoice.objects.filter(
        organization=organization, period=period
    ).exists():
        return

    ledgers = SavingsLedger.objects.filter(
        cloud_account__organization=organization,
        period_start__startswith=period,
    )

    if not ledgers.exists():
        return

    total_savings = ledgers.aggregate(
        total=Sum("amount")
    )["total"] or Decimal("0")

    revenue = RevenueShare.objects.filter(
        organization=organization,
        savings_event__in=ledgers,
    )

    platform_fee = revenue.aggregate(
        total=Sum("amount_due")
    )["total"] or Decimal("0")

    invoice = Invoice.objects.create(
        organization=organization,
        period=period,
        total_savings=total_savings,
        platform_fee=platform_fee,
        status="issued",
        issued_at=timezone.now(),
    )

    for ledger in ledgers:
        share = RevenueShare.objects.get(savings_event=ledger)

        InvoiceLineItem.objects.create(
            invoice=invoice,
            savings_ledger=ledger,
            gross_savings=ledger.amount,
            platform_fee=share.amount_due,
        )

    return invoice
