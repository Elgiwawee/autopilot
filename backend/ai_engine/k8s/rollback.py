# ai_engine/k8s/rollback.py

def should_rollback(metrics):
    return (
        metrics.latency_increase > 0.1
        or metrics.restart_spike
    )
