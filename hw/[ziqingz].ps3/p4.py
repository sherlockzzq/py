def distance(point1, point2):
	sum = 0
	if point2 == 0:
		for i in point1:
			sum += int(i) ** 2
		return sum ** 0.5
	for i in len(point1):
		sum += (int(point1[i]) - int(point2[i])) ** 2
	return sum ** 0.5

l = input('Enter a point: ')
listA = []
while l:
	li = l.split(',')
	li.append(distance(li, 0))
	listA.append(li)
	l = input('Enter a point: ')
path = input('Enter a destination file path: ')
fp = open(path, 'w')
listA.sort(key = lambda x: x[-1])


for i in range(len(listA)):
	str1 = ''
	for j in range(len(listA[0]) - 1):
		str1 += str(listA[i][j]) + ','
	fp.writelines('({a}): {b}\n'.format(a = str1[:-1], b = listA[i][-1]))

fp.close()
