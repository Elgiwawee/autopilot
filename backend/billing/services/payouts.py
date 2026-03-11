# billing/services/payouts.py

from billing.models import RevenueShare, Invoice


def settle_revenue_share(invoice: Invoice):
    shares = RevenueShare.objects.filter(
        organization=invoice.organization,
        paid=False,
    )

    for share in shares:
        share.paid = True
        share.save(update_fields=["paid"])
