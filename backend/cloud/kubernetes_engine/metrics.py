# cloud/kubernetes_engine/metrics.py

def parse_cpu(v: str) -> int:
    """
    Returns millicores
    """
    if v.endswith("m"):
        return int(v[:-1])
    return int(float(v) * 1000)


def parse_mem(v: str) -> int:
    """
    Returns MB
    """
    if v.endswith("Mi"):
        return int(v[:-2])
    if v.endswith("Gi"):
        return int(float(v[:-2]) * 1024)
    return 0


def extract_requests(pod):
    cpu = 0
    mem = 0

    for c in pod.spec.containers:
        if c.resources and c.resources.requests:
            cpu += parse_cpu(c.resources.requests.get("cpu", "0"))
            mem += parse_mem(c.resources.requests.get("memory", "0"))

    return cpu, mem


def extract_usage(metric):
    cpu = 0
    mem = 0

    for c in metric["containers"]:
        cpu += parse_cpu(c["usage"]["cpu"])
        mem += parse_mem(c["usage"]["memory"])

    return cpu, mem
