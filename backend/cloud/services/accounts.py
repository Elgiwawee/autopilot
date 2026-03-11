# cloud/services/accounts.py

from cloud.models import CloudAccount


def get_active_cloud_accounts(organization):
    """
    Returns active cloud accounts for an organization.
    """
    return CloudAccount.objects.filter(
        organization=organization,
        is_active=True
    ).select_related("provider")