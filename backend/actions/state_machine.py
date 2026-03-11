ALLOWED_TRANSITIONS = {
    "DETECTED": ["PLANNED"],
    "PLANNED": ["SIMULATED"],
    "SIMULATED": ["APPROVED"],
    "APPROVED": ["EXECUTING"],
    "EXECUTING": ["VERIFIED", "FAILED"],
    "VERIFIED": ["COMPLETED", "ROLLED_BACK"],
}

def assert_transition(current, next_state):
    if next_state not in ALLOWED_TRANSITIONS.get(current, []):
        raise ValueError(f"Invalid transition {current} → {next_state}")
