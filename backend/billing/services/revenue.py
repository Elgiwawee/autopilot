# billing/services/revenue.py

from decimal import Decimal
from django.db import transaction
from billing.models import RevenueShare, SavingsLedger

DEFAULT_PLATFORM_PCT = Decimal("20.0")


@transaction.atomic
def create_revenue_share_from_ledger(ledger: SavingsLedger):
    """
    Creates platform revenue share from a finalized savings ledger entry.
    This is NON-OPTIONAL and NON-BYPASSABLE.
    """

    # Prevent duplicates
    if RevenueShare.objects.filter(savings_event=ledger).exists():
        return

    pct = Decimal(DEFAULT_PLATFORM_PCT)

    amount_due = (Decimal(ledger.amount) * pct) / Decimal("100")

    RevenueShare.objects.create(
        organization=ledger.cloud_account.organization,
        savings_event=ledger,
        pct=float(pct),
        amount_due=amount_due,
    )
