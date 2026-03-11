# ai_engine/storage/gp3_rules.py

def gp2_to_gp3_candidate(volume):
    if volume.volume_type != "gp2":
        return False

    if volume.state != "in-use":
        return False

    return True
