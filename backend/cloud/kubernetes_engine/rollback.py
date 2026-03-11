# cloud/kubernetes_engine/rollback.py

from audit.services.receipt import generate_execution_receipt


def rollback_execution(
    *,
    k8s,
    deployment_name: str,
    namespace: str,
    previous_spec: dict,
    reason: str,
    policy,
):
    """
    Roll back deployment to previous spec
    """

    k8s.apps.patch_namespaced_deployment(
        name=deployment_name,
        namespace=namespace,
        body=previous_spec,
    )

    generate_execution_receipt(
        action="K8S_ROLLBACK",
        status="ROLLED_BACK",
        policy_id=policy.id,
        target=f"{namespace}/{deployment_name}",
        message=reason,
    )
