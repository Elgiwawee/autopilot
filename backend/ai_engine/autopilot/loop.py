# ai_engine/autopilot/loop.py

from celery import shared_task
from ai_engine.autopilot.state import AutopilotState
from ai_engine.autopilot.safety import kill_switch_enabled
from ai_engine.autopilot.rollback import rollback_if_needed


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=30)
def autopilot_loop(self, scope="default"):
    if kill_switch_enabled():
        return "Autopilot disabled by kill switch"

    collect_metrics(scope)
    generate_plans(scope)

    if can_act(scope):
        execute_safe_actions(scope)

    verify_health(scope)

    if health_failed(scope):
        rollback_if_needed(scope)


CELERY_BEAT_SCHEDULE = {
    "autopilot-k8s": {
        "task": "ai_engine.autopilot.loop.autopilot_loop",
        "schedule": crontab(minute="*/15"),
        "args": ("k8s",),
    },
    "autopilot-nodes": {
        "task": "ai_engine.autopilot.loop.autopilot_loop",
        "schedule": crontab(hour="*/1"),
        "args": ("nodes",),
    },
    "autopilot-storage": {
        "task": "ai_engine.autopilot.loop.autopilot_loop",
        "schedule": crontab(hour=0),
        "args": ("storage",),
    },
}
