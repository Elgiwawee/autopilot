# control_plane/services/audit_service.py

from audit.services.logs import get_audit_logs


def build_audit(organization):
    return {
        "organization": organization.id,
        "logs": get_audit_logs(organization),
    }
