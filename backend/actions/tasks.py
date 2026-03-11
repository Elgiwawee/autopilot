# actions/tasks.py

from celery import shared_task
from actions.models import ActionExecution
from actions.executors.aws_ec2 import stop_ec2_instance


@shared_task(bind=True)
def execute_action(self, action_execution_id):
    execution = ActionExecution.objects.get(id=action_execution_id)
    resource = execution.action_plan.resource

    execution.status = "executing"
    execution.save()

    try:
        stop_ec2_instance(resource, credentials=...)  # assume role again
        execution.status = "success"
        execution.executed_at = now()
        execution.save()

    except Exception as e:
        execution.status = "failed"
        execution.error_message = str(e)
        execution.save()
        raise
