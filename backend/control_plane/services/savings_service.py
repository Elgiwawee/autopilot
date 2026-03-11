# control_plane/services/savings_service.py

from billing.services.savings_service import get_savings_summary


def build_savings(organization):
    return {
        "organization": organization.id,
        "summary": get_savings_summary(organization),
    }
