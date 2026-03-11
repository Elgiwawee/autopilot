# control_plane/services/billing_guard.py

from billing.models import Invoice


def assert_billing_in_good_standing(organization):
    unpaid = Invoice.objects.filter(
        organization=organization,
        status__in=["issued", "overdue"],
    ).exists()

    if unpaid:
        raise RuntimeError(
            "Autopilot execution blocked: outstanding invoice"
        )
