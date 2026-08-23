import numpy as np

def gauss_seidel(A, b, n, x_ini=None):

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    # Initial guess
    if x_ini is None:
        x = np.zeros(len(b))
    else:
        x = np.array(x_ini, dtype=float)

    # Perform n iterations
    for _ in range(n):

        for i in range(len(A)):

            # Start with b[i]
            total = b[i]

            # Subtract all other terms
            for j in range(len(A)):
                if i != j:
                    total -= A[i][j] * x[j]

            # Update x[i]
            x[i] = total / A[i][i]

    return x
