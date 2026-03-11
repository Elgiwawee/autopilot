# ai_engine/autopilot/tasks.py
from celery import shared_task
from accounts.models import Organization
from ai_engine.autopilot_engine import AutopilotEngine


@shared_task(bind=True)
def autopilot_loop(self):

    engine = AutopilotEngine()

    for org in Organization.objects.all():
        engine.run_for_organization(org)