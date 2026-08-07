import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	if len(v1)!= len(v2):
		return -1

	# Dot product
	result = 0
	for i in range(len(v1)):
		result+= v1[i] * v2[i]

	# Magnitude of v1
	modev1 = 0 
	for x in v1:
		modev1 += x**2
	modev1 = modev1**0.5

	# Magnitude of v2 
	modev2 = 0
	for y in v2:
		modev2 += y**2
	modev2 = modev2**0.5


	if modev1 == 0 or modev2 == 0:
		return -1

	return result / (modev1 * modev2)