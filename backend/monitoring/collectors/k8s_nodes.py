# monitoring/collectors/k8s_nodes.py

from kubernetes import client, config
from monitoring.models import NodeMetric

def collect_node_metrics(cluster_id):
    config.load_kube_config()

    core = client.CoreV1Api()
    metrics = client.CustomObjectsApi()

    node_metrics = metrics.list_cluster_custom_object(
        group="metrics.k8s.io",
        version="v1beta1",
        plural="nodes",
    )

    for item in node_metrics["items"]:
        name = item["metadata"]["name"]

        cpu_used = int(item["usage"]["cpu"].replace("n", "")) / 1e9
        mem_used = int(item["usage"]["memory"].replace("Ki", "")) // 1024

        node = core.read_node(name)
        cpu_total = int(node.status.capacity["cpu"])
        mem_total = int(node.status.capacity["memory"].replace("Ki", "")) // 1024

        NodeMetric.objects.create(
            cluster_id=cluster_id,
            node_name=name,
            cpu_used=cpu_used,
            cpu_total=cpu_total,
            mem_used=mem_used,
            mem_total=mem_total,
        )
