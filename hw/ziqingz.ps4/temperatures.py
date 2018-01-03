def convert_temperatures(*para, degree = 'degree'):
	list1 = list(para)
	res = []
	if degree == 'Celsius':
		res = list(map(celsius_to_fahrenheit, list1))
	elif degree == 'Fahrenheit':
		res = [fahrenheit_to_celsius(x) for x in list1]
	return res

def fahrenheit_to_celsius(x):
	return (x - 32) / 1.8

def celsius_to_fahrenheit(x):
	return x * 1.8 + 32
