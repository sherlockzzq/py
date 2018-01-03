import math
def quadratic(A, B, C):
	delta = B ** 2 - 4 * A * C
	if delta < 0 :
		return None
	return (-B + math.sqrt(delta))/(2*A), (-B - math.sqrt(delta))/(2*A)
