import numpy as np

def reshape_array(data: list, operation: str) -> np.ndarray:
    """
    Returns a float64 array with the shape selected by operation.
    """
    pass
    a = np.array(data, dtype=np.float64)
    if operation == "flatten":
        return a.flatten()
    elif operation == "transpose":
        return a.T
    elif operation == "add_batch":
        return a.reshape(1, a.shape[0], a.shape[1])