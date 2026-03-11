# ai_engine/gpu/features.py

import numpy as np

def extract_features(metrics):
    utilizations = [m.utilization for m in metrics]

    return [
        np.mean(utilizations),
        np.percentile(utilizations, 95),
        np.std(utilizations),
    ]
