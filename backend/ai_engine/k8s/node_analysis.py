# ai_engine/k8s/node_analysis.py

from django.utils.timezone import now, timedelta
from monitoring.models import NodeMetric
from ai_engine.k8s.node_waste import calculate_waste


def analyze_node(node_name):
    since = now() - timedelta(days=14)
    metrics = NodeMetric.objects.filter(node_name=node_name, timestamp__gte=since)

    avg_cpu_used = sum(m.cpu_used for m in metrics) / len(metrics)
    avg_cpu_total = metrics[0].cpu_total

    avg_mem_used = sum(m.mem_used for m in metrics) / len(metrics)
    avg_mem_total = metrics[0].mem_total

    return calculate_waste(
        avg_cpu_used,
        avg_cpu_total,
        avg_mem_used,
        avg_mem_total,
    )
