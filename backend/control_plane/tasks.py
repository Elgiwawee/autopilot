from celery import shared_task
from django.db import transaction

from accounts.models import Organization
from cloud.models import CloudAccount

from ai_engine.autopilot_engine import AutopilotEngine
from cloud.collectors.aws_ec2 import collect_ec2_instances


@shared_task(bind=True)
def run_autopilot_for_org(self, organization_id):
    """
    Trigger the full autopilot engine for an organization.
    """

    org = Organization.objects.get(id=organization_id)

    engine = AutopilotEngine()

    engine.run_for_organization(org)


@shared_task(bind=True)
def discover_cloud_account(self, cloud_account_id):
    """
    Run infrastructure discovery when a cloud account is connected.
    """

    account = CloudAccount.objects.get(id=cloud_account_id)

    if account.provider.code == "aws":
        collect_ec2_instances(account.id)