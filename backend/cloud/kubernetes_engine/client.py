# cloud/kubernetes_engine/client.py

from kubernetes import client, config

class KubernetesClient:
    def __init__(self, kubeconfig_path=None):
        if kubeconfig_path:
            config.load_kube_config(kubeconfig_path)
        else:
            config.load_incluster_config()

        self.core = client.CoreV1Api()
        self.apps = client.AppsV1Api()
        self.custom = client.CustomObjectsApi()
