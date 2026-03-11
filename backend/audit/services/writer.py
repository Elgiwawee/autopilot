# audit/services/writer.py

from audit.models import AuditLog


def write_audit_log(
    *,
    organization,
    actor,
    action,
    resource_id,
    status,
    metadata=None,
):
    """
    Immutable audit writer.
    This is the ONLY place where audit logs are created.
    """

    AuditLog.objects.create(
        organization=organization,
        actor=actor,
        action=action,
        resource_id=resource_id,
        status=status,
        metadata=metadata or {},
    )
