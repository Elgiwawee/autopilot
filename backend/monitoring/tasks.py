from celery import shared_task
from monitoring.health import verify_system_health as run_health_check


@shared_task
def verify_system_health():
    """
    Celery task for periodic system health checks.
    """

    return run_health_check()