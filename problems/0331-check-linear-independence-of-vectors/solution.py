import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
        
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    # Empty set is linearly independent
    if len(vectors) == 0:
        return True

    # Convert vectors to columns
    A = np.array(vectors, dtype=float).T

    rows, cols = A.shape
    rank = 0
    tol = 1e-10

    for col in range(cols):

        # No more rows available for pivots
        if rank == rows:
            break

        # Find pivot row
        pivot_row = np.argmax(np.abs(A[rank:, col])) + rank

        # If pivot is approximately zero, no pivot in this column
        if abs(A[pivot_row, col]) <= tol:
            continue

        # Swap rows
        A[[rank, pivot_row]] = A[[pivot_row, rank]]

        # Eliminate values below pivot
        for row in range(rank + 1, rows):
            factor = A[row, col] / A[rank, col]
            A[row] -= factor * A[rank]

        rank += 1

        # If rank equals number of vectors
        if rank == cols:
            break

    return rank == cols