import numpy as np


 
def make_diagonal(x):
	result = np.zeros((len(x),len(x)))

	for i in range(len(x)):
		for j in range(len(x)):
			if j == i:
				result[i][j] = x[i]

    
	return result
	 