
# ai_engine/k8s/binpacking.py
def binpacking_efficiency(used_cpu, total_cpu):
    return round((used_cpu / total_cpu) * 100, 2)


def recommend_node_type(avg_cpu, avg_mem):
    if avg_cpu < 2 and avg_mem < 4096:
        return "t3.large"
    if avg_cpu < 4:
        return "m6i.large"
    return "m6i.xlarge"


def spot_allowed(workload):
    return workload.replicas >= 2
