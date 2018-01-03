import math
def triangle(**para): 
	val = list(para.values())
	return 1/2 * val[0] * val[1]
def rectangle(**para):
	val = list(para.values())
	return val[0] * val[1]
def circle(**para):
	val = list(para.values())
	if "radius" in para.keys():
		return math.pi*val[0]**2
	else:
		return math.pi*(val[0]/2)**2
def area(shape, **para):
	dict = {'circle': circle, 'rectangle': rectangle, 'triangle':triangle} 
	

	return dict[shape](**para)
