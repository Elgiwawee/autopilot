def simulate_stop(instance):
    return {
        "impact": "Instance will stop",
        "downtime": "None (non-prod)",
        "dependencies": [],
        "rollback": "StartInstance"
    }
