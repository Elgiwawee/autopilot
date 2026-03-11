# ai_engine/time_gate.py

from datetime import datetime
import pytz


def within_maintenance_window(org):
    window = org.maintenancewindow_set.first()
    if not window:
        return False

    now = datetime.now(pytz.timezone(window.timezone)).time()
    return window.start_time <= now <= window.end_time
