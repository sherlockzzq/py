import sys
def fibonacci(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		n = fibonacci(n - 1) + fibonacci(n - 2)
		return n
for i in range(int(sys.argv[1])+1):
	print(fibonacci(i))
