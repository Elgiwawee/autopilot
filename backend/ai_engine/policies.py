# ai_engine/policies.py

def autopilot_policy_check(resource, action_type):
    """
    Global safety rules.
    """

    # Never touch production-tagged resources (for now)
    tags = resource.metadata.get("Tags", [])
    for tag in tags:
        if tag.get("Key") == "Environment" and tag.get("Value") == "production":
            return False, "Production resource"

    # Only allow STOP on idle VMs
    if action_type == "stop" and resource.state != "running":
        return False, "Instance not running"

    return True, "Policy passed"

"""
Later: Time windows, maintenance windows,SLO-based gates,budget limits 

"""