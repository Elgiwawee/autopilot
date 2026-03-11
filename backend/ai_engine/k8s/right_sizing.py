# ai_engine/k8s/right_sizing.py

def recommended_cpu_request(p95_cpu):
    return round(p95_cpu * 1.3, 2)  # 30% headroom


def recommended_mem_request(p95_mem):
    return int(p95_mem * 1.2)  # memory OOM = death


def autopilot_allowed(workload):
    return (
        workload.replicas >= 2
        and not workload.namespace.startswith("kube")
    )
