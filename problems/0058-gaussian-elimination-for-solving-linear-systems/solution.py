import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	#Step 1: Convert to floating-point NumPy arrays
	A = np.array(A,dtype=float)
	b = np.array(b,dtype=float)

	# Number of equcations
	n = len(b)

	# -------------------------------
    # Gaussian Elimination
    # -------------------------------
	for k in range(n-1):
		# Step 2: Find the pivot row
		pivot = np.argmax(np.abs(A[k:,k])) + k

		# Step 3: Swap rows if necessary
		if pivot!=k:
			A[[k,pivot]] = A[[pivot,k]]
			b[[k,pivot]] = b[[pivot,k]]

		# Step 4 : Eliminate values below pivot
		for i in range(k+1,n):

			# Calculate mutliplier
			factor = A[i,k]/A[k,k]

			# Make the element below pivot zero
			A[i,k:] = A[i,k:] - factor * A[k,k:]

			# Apply same operation to b
			b[i] = b[i] - factor * b[k]

	# -------------------------------
    # Backward Substitution
    # -------------------------------

	# Create solution vector 
	x = np.zeros(n)

	# Start from bottom row and move upward
	for i in range(n-1,-1,-1):

		# Calculate already-known part
		sum_ax = np.dot(A[i,i+1:] , x[i+1:])

		# Calculate current variable
		x[i] = (b[i] - sum_ax) / A[i,i]

	

	return x
