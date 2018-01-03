str1 = input('Please enter an integer:')
count = 0
listAll = []
while str1:
	num = int(str1)
	listAll.append([num, count])
	str1 = input('Please enter an integer:')
	count += 1
listAll.sort()
for i in range(0, len(listAll)):
	print(listAll[i][0], '({})'.format(listAll[i][1]))
