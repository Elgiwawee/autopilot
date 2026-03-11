import boto3
from celery import shared_task
from actions.models import ActionExecution
from monitoring.health_checks import verify_resource_health

def rollback_stop_instance(resource, credentials):
    ec2 = boto3.client(...)
    ec2.start_instances(InstanceIds=[resource.external_id])


@shared_task
def monitor_and_rollback(action_execution_id):
    execution = ActionExecution.objects.get(id=action_execution_id)
    resource = execution.action_plan.resource

    healthy = verify_resource_health(resource)

    if not healthy:
        rollback_stop_instance(resource, credentials=...)
        execution.status = "rolled_back"
        execution.save()
