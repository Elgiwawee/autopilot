# accounts/services/autopilot_service.py

from accounts.models import GlobalSafety, AutopilotSettings


class AutopilotService:

    @staticmethod
    def get_effective_status(organization, cloud=None):

        global_safety = GlobalSafety.objects.first()

        autopilot_settings = None

        if cloud:
            autopilot_settings = AutopilotSettings.objects.filter(
                cloud_account__provider__slug=cloud
            ).first()

        global_enabled = bool(
            global_safety and global_safety.autopilot_enabled
        )

        mode = (
            autopilot_settings.mode
            if autopilot_settings
            else "OBSERVE"
        )

        max_risk = (
            autopilot_settings.max_risk_allowed
            if autopilot_settings
            else None
        )

        effective = (
            "ACTIVE"
            if global_enabled and mode != "OBSERVE"
            else "PAUSED"
        )

        return {
            "global_enabled": global_enabled,
            "mode": mode,
            "max_risk_allowed": max_risk,
            "effective_status": effective,
        }