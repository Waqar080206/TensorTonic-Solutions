import numpy as np

def one_hot(y, num_classes=None):
    y = np.asarray(y, dtype=int)

    if num_classes is None:
        num_classes = np.max(y) + 1

    if np.any(y < 0) or np.any(y >= num_classes):
        raise ValueError("Labels must satisfy 0 <= y < num_classes")

    n = len(y)
    out = np.zeros((n, num_classes), dtype=float)
    out[np.arange(n), y] = 1.0

    return out