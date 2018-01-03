def my_reduce(function, iterable):
	iterator = iter(iterable)
	value = next(iterator)
	for i in iterator:
		value = function(value, i)
	return value