# ai_engine/spot/features.py

def extract_features(event):
    return [
        event.timestamp.hour,
        event.timestamp.weekday(),
        hash(event.instance_type) % 1000,
        hash(event.availability_zone) % 100,
    ]
