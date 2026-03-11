# ai_engine/chaos/simulator.py

from actions import models


def simulate_failure(action):
    if action.type == "resize":
        return "cpu_spike"
    if action.type == "spot":
        return "node_loss"


class ActionPlan:
    dry_run = models.BooleanField(default=True)


def confidence_after_simulation(success_rate):
    return success_rate * 100
