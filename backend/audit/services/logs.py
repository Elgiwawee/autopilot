# audit/services/logs.py

from audit.models import AuditLog


def get_audit_logs(organization, limit=50):
    logs = (
        AuditLog.objects
        .filter(organization=organization)
        .order_by("-created_at")[:limit]
    )

    return [
        {
            "id": str(log.id),
            "timestamp": log.created_at.isoformat(),
            "actor": log.actor,
            "action": log.action,
            "resource_id": log.resource_id,
            "cloud": log.metadata.get("cloud") if log.metadata else None,
            "status": log.status,
        }
        for log in logs
    ]
