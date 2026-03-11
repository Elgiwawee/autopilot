from django.utils.timezone import now
from audit.models import AuditEvent

def execute_stop(execution, aws_client):
    execution.state = "EXECUTING"
    execution.started_at = now()
    execution.save()

    try:
        aws_client.stop_instances(
            InstanceIds=[execution.rollback_payload["instance_id"]]
        )

        execution.after_state = fetch_instance_state(...)
        execution.state = "VERIFIED"

    except Exception as e:
        execution.error = str(e)
        execution.state = "FAILED"

    execution.save()



AuditEvent.objects.create(
    cloud_account=execution.decision.plan.cloud_account,
    actor="SYSTEM",
    event_type="ACTION_EXECUTED",
    resource_type="EC2",
    resource_id=instance_id,
    before_state=execution.before_state,
    after_state=None,
    metadata={
        "execution_id": str(execution.id),
        "risk_score": execution.decision.risk_score,
    },
)
