def get_pod_metrics(api):
    return api.list_pod_metrics_for_all_namespaces()
