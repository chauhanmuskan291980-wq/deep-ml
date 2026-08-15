import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """

    # Make the copy , so the original matrix is not elimination. 
    A = A.astype(float).copy()
    rows , cols = A.shape
    rank = 0

    for col in range(cols):
        # Find the row with the larget value in the column
        pivot_row = np.argmax(np.abs(A[rank:,col])) + rank

        # If pivot is approximately zero , skip this column
        if abs(A[pivot_row,col] <=tol):
            continue
        
        # Swap pivot row with the current rank row
        A[[rank, pivot_row]] = A[[pivot_row, rank]]

        # Eliminate values below the pivot

        for row in range(rank+1, rows):
            factor = A[row,col]/A[rank,col]
            A[row] -= factor*A[rank]

        rank +=1

        # Stop if all rows have pivotes
        if rank == rows:
            break
    
    return rank









    pass