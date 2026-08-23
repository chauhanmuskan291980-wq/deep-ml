import numpy as np

def cramers_rule(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    # Calculate determinant of A
    det_A = np.linalg.det(A)

    # If determinant is zero, no unique solution
    if np.isclose(det_A, 0):
        return -1

    n = len(A)
    x = []

    # Replace each column one by one
    for i in range(n):
        A_i = A.copy()

        # Replace column i with b
        A_i[:, i] = b

        # Calculate determinant of modified matrix
        det_Ai = np.linalg.det(A_i)

        # Cramer's Rule
        x_i = det_Ai / det_A

        x.append(x_i)

    return np.round(x, 4)