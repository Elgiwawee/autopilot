from accounts.models import AutopilotSettings, GlobalSafety


def assert_autopilot_allowed(cloud_account, risk_score, action):
    """
    Centralized autopilot enforcement.
    """

    # Global switch
    global_safety = GlobalSafety.objects.first()
    if not global_safety or not global_safety.autopilot_enabled:
        raise RuntimeError("Autopilot globally disabled")

    settings = AutopilotSettings.objects.filter(
        cloud_account=cloud_account
    ).first()

    if not settings:
        raise RuntimeError("Autopilot settings not configured")

    # OFF mode
    if settings.mode == "OFF":
        raise RuntimeError("Autopilot is OFF")

    # RECOMMEND mode
    if settings.mode == "RECOMMEND":
        raise RuntimeError("Autopilot in recommendation-only mode")

    # Risk threshold
    if risk_score > settings.max_risk_allowed:
        raise RuntimeError("Risk exceeds allowed threshold")

    # Safe mode restrictions
    if settings.mode == "AUTO_SAFE":
        if action in ["DELETE", "TERMINATE"]:
            raise RuntimeError(
                "Destructive actions blocked in AUTO_SAFE mode"
            )

    # AUTO_AGGRESSIVE allows everything within risk threshold
