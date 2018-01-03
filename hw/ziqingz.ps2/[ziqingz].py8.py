listAll = []
with open('/Users/zhangziqing/Desktop/fangraphs_leaderboard.csv', encoding='utf-8-sig') as csv:
	fp = csv.readline()
	col = fp.replace('"', '').split(',')
	for line in csv:
		listAll.append(line.replace('"', '').split(',')) 
ctg = input('Enter an offensive category:')
name = [i[0] for i in listAll]
if ctg not in col:
	print('Error:\nCategory not available')
else:
	back = col.index(ctg)
	scores = [float(a) for a in [i[back] for i in listAll]]
	index = [i[1] for i in sorted([[scores[i], i] for i in range(0, len(scores))], reverse = True)]
	print('Result:')
	for j in range(0, 5) :
		print('{n}, {h}'.format(n = name[index[j]], h = int(scores[index[j]]) if int(scores[index[j]]) == scores[index[j]] else scores[index[j]]))

