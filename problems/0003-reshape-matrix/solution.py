import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    if (new_shape[0]*new_shape[1]!=len(a[0])*len(a)):
	    return []
	arr = np.array(a)
	reshaped_arr = arr.reshape(new_shape)
	reshaped_matrix = reshaped_arr.tolist()

	return reshaped_matrix