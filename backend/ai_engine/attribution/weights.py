# ai_engine/attribution/weights.py
def compute_weights(usages):
    total = sum(
        u.cpu_hours * 0.7 + u.memory_gb_hours * 0.3
        for u in usages
    )

    for u in usages:
        u.weight = (
            (u.cpu_hours * 0.7 + u.memory_gb_hours * 0.3) / total
            if total else 0
        )
