# ai_engine/k8s/node_planner.py

def recommend_nodegroup_size(avg_pods, cpu_per_pod, mem_per_pod):
    cpu_needed = avg_pods * cpu_per_pod
    mem_needed = avg_pods * mem_per_pod

    if cpu_needed < 4 and mem_needed < 16_000:
        return "m6i.large"
    if cpu_needed < 8:
        return "m6i.xlarge"
    return "m6i.2xlarge"
