path_1 = input('Please enter file path 1:')
path_2 = input('Please enter file path 2:')
output1 = open(path_1)
output2 = open(path_2)
list1 = []
list2 = []
line1 = output1.readline()
line2 = output2.readline()
while(line1):
	list1.append(line1)
	line1 = output1.readline()
while(line2):
	list2.append(line2)
	line2 = output2.readline()
count = 0
string = ''
while(count < len(list2) and count < len(list1)):
	if list2[count].strip('\n') != list1[count].strip('\n'):
		string = '{}{}, '.format(string, count)
	count += 1
while(count < len(list1) or count < len(list2)):
	string = '{}{}, '.format(string, count)
	count += 1

print(string[:-2])
output2.close()
output1.close()
