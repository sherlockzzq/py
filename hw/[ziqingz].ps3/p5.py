
def number_manipulation_maker(operation, y):
	def add(x):
		return x + y
	def substract(x):
		return x - y
	def multiply(x):
		return x * y
	def divide(x):
		return x / y
	def exponent(x):
		return x ** y	
	dict = {'add': add, 'substract':substract, 'multiply':multiply, 'divide':divide}
	return dict[operation]
