# billing/tasks/invoicing.py

from celery import shared_task
from django.utils.timezone import now
from accounts.models import Organization
from billing.services.invoicing import generate_monthly_invoice


@shared_task
def generate_all_invoices():
    period = now().strftime("%Y-%m")

    for org in Organization.objects.all():
        generate_monthly_invoice(org, period)
