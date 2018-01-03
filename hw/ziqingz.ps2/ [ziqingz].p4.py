str1 = input('Please enter a string:')
str1 = str1.lower()
list1 = []
for s in str1:
	if('a' <= s <= 'z'):
		list1.append(s)
start, end = 0, len(list1) - 1
while start < end:
	if(list1[start] != list1[end]):
		print('False')
		break
	start += 1
	end -= 1
else:
	print('True')
