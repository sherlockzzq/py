import random
def getPi(n):
	count = 0
	for i in range(0, n):
		x = random.random()
		y = random.random()
		if (x ** 2 + y ** 2) ** 0.5 <= 1:
			count += 1
	return count / n * 4