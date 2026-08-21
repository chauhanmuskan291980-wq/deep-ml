import numpy as np

def rref(matrix):
	A = np.array(matrix,dtype=float)

	rows ,cols = A.shape
	pivot_row = 0

	for col in range(cols):
		# Step 1: Find a non-zero pivot
		pivot = pivot_row

		while pivot < rows and A[pivot,col] == 0:
			pivot +=1
		
		# No pivot found in the column
		if pivot == rows:
			continue

		# Step 2 : Swap rows if necessary
		A[[pivot_row,pivot]] = A[[pivot,pivot_row]]

		# Step 3 : Make the pivot equal to 1
		A[pivot_row] = A[pivot_row] / A[pivot_row,col]

		# Step 4: Make all other values in pivot column zero 
		for row in range(rows):
			if row!=pivot_row:
				A[row] = A[row] - A[row,col] * A[pivot_row]

		# Move to the next pivot row
		pivot_row +=1

		# Stop if we have processed all rows
		if pivot_row == rows:
			break

	# Remove very samll floating point values 
	A[np.abs(A)<1e-10] =0
	return A

