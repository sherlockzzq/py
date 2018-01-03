import re
path = input('Please enter a file path:')
input1 = open(path, encoding = 'utf-8-sig')
lines = input1.readlines()
dic = {}
count = 0
lcount = 0
for line in lines:
		lcount += 1
		line = re.sub(r'[^\w\s]','',line)
		words = line.lower().split()
		for word in words:
			if word in dic:
				dic[word] = dic[word] + 1
			else:
				dic[word] = 1
			count += 1
listAll = []
for element in dic:
	listAll.append([dic[element], element])
listAll.sort()
print('File stats:\nWord count: {a}\nLine count: {b}\nMost frequent words: '.format(a = count, b = lcount))
length = len(listAll) - 1
print(listAll[length][1], '({b})'.format(b = listAll[length][0]))
print(listAll[length - 1][1], '({b})'.format(b = listAll[length - 1][0]))
input1.close()
