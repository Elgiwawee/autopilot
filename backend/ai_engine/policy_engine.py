# ai_engine/policy_engine.py

from accounts.models import AutopilotPolicy

def evaluate_policy(resource, action_type):
    org_policy = resource.cloud_account.organization.autopilot_policy

    if not org_policy:
        return False, "No autopilot policy defined"

    if org_policy.enable_kill_switch:
        return False, "Autopilot kill switch enabled"

    if action_type == "stop" and not org_policy.allow_stop:
        return False, "Stop actions disabled by policy"

    if action_type == "resize" and not org_policy.allow_resize:
        return False, "Resize actions disabled by policy"

    if action_type == "delete" and not org_policy.allow_delete:
        return False, "Delete actions disabled by policy"

    return True, "Policy approved"
