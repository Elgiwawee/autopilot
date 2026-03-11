# ai_engine/storage/utilization.py
def underutilized_volume(volume, avg_iops):
    if avg_iops is None:
        return False

    if avg_iops < 100:
        return True

    return False
