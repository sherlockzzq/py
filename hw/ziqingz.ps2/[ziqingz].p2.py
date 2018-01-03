str1 = input('Please enter a string:')
list1 = []
while str1:
	list1.append(str1.lower().strip())
	str1 = input('Please enter a string:')
list1.sort()
print('You entered:')
print(', '.join(list1))
