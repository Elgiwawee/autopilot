# ai_engine/autopilot/state.py

from enum import Enum


class AutopilotState(str, Enum):
    OBSERVE = "observe"
    SIMULATE = "simulate"
    ACT = "act"
    VERIFY = "verify"
    ROLLBACK = "rollback"
