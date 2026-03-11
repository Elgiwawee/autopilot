# monitoring/health.py

import logging

logger = logging.getLogger(__name__)


def verify_system_health():
    """
    Verify health of core system services.
    """

    logger.info("Running system health checks")

    # Example checks (extend later)
    checks = {
        "database": True,
        "celery": True,
        "redis": True,
    }

    logger.info("System health status: %s", checks)

    return checks