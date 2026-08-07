import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', or 'frobenius')

    Returns:
        The computed norm as a float.
    """

    # Detect if arr is a matrix (2D) or a vector (1D)
    is_matrix = arr.ndim == 2

    # Flatten the matrix into a 1D array
    if is_matrix:
        flat_data = arr.flatten()
    else:
        flat_data = arr

    # L1 Norm (sum of absolute values)
    if norm_type == "l1":
        return sum(abs(x) for x in flat_data)

    # L2 Norm (Euclidean norm)
    elif norm_type == "l2":
        return sum(x**2 for x in flat_data) ** 0.5

    # Frobenius Norm (for matrices)
    elif norm_type == "frobenius":
        return sum(x**2 for x in flat_data) ** 0.5

    else:
        raise ValueError("Invalid norm type. Choose 'l1', 'l2', or 'frobenius'.")

  