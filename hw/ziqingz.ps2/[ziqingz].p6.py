import math

point = input('Enter a point:')
point_list = []
while point:
	nums = point.split(',')
	x, y = int(nums[0]), int(nums[1])
	distance = math.sqrt(x ** 2 + y ** 2)
	point_list.append([int(distance) if distance == int(distance) else distance, x, y])
	point = input('Enter a point:')
path = input('Enter a destination file path:')
fp = open(path, 'w')
point_list.sort()

for i in range(0, len(point_list)):
	fp.writelines('({a}, {b}): {c}\n'.format(a = point_list[i][1], b = point_list[i][2], c = point_list[i][0]))
fp.close()
