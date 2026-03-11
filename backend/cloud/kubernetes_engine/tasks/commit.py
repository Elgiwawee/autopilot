# kubernetes_engine/tasks/commit.py

from celery import shared_task
from django.utils import timezone
from actions.models import ExecutionRecord


@shared_task(bind=True)
def commit_execution(self, execution_record_id):
    execution = ExecutionRecord.objects.get(id=execution_record_id)

    execution.state = "COMPLETED"
    execution.finished_at = timezone.now()
    execution.save(update_fields=["state", "finished_at"])
