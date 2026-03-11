# ai_engine/resize_rules.py

def resize_safe(resource, utilization):
    """
    Conservative rules for production safety.
    """

    if utilization["cpu_avg"] is None:
        return False, "No CPU data"

    if utilization["cpu_avg"] > 30:
        return False, "CPU average too high"

    if utilization["cpu_max"] and utilization["cpu_max"] > 60:
        return False, "CPU spikes detected"

    return True, "Safe to downsize"
