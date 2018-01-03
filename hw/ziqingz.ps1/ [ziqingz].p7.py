import csv
listAll = []
name = input('Enter a player name: ')
ctg = input('Enter an offensive category: ')
with open('/Users/zhangziqing/Desktop/fangraphs_leaderboard.csv', encoding='utf-8-sig') as csvfile:
	fp = csv.reader(csvfile)
	for row in fp:
		listAll.append(row)
namelist = [col[0] for col in listAll]
if name not in namelist:
	print('Error:\nPlayer not found')
else:
	catogary = listAll[0]
	if ctg not in catogary:
		print('Error:\nCategory not available')
	else:
		Id = namelist.index(name)
		ctgId = catogary.index(ctg)
		print("Result:\n{a} {b} {c}: {d}".format(a = name, b = listAll[Id][1], c = ctg, d = listAll[Id][ctgId]))
