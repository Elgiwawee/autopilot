# ai_engine/services/recommendation_service.py

from cloud.models import CloudResource
from ai_engine.planner import generate_action_plans


def generate_recommendations(account, metrics):

    resources = CloudResource.objects.filter(
        cloud_account=account
    )

    plans = []

    for resource in resources:
        plans.extend(generate_action_plans(resource))

    return plans

#plug in many AI modules later
"""
generate_idle_ec2_recommendations()
generate_rightsize_ec2()
generate_k8s_binpacking()
generate_spot_rebalance()
generate_gpu_idle_detection()
"""
