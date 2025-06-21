import numpy as np


def are_all_values_equal(arr: np.ndarray) -> bool:
    if arr.size == 0:
        return True

    return all(x == arr[0] for x in arr)
