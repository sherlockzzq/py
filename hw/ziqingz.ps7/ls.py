#!/usr/bin/env python3
import sys
import os
import stat
from pathlib import Path
import datetime
import time
import re


path = Path.cwd()
if len(sys.argv) > 1:
	path = sys.argv[1]
p = Path(path)
def run(p):
	try:
		if not os.path.exists(p):
			raise FileNotFoundException

	except FileNotFoundException:
		print('ls: cannot access \'{}\': No such file or directory'.format(p))
		return
	def unix_datetime(): #Reference: https://stackoverflow.com/questions/10256093/how-to-convert-ctime-to-datetime-in-python
		return datetime.datetime.fromtimestamp(float(os.stat(file).st_ctime)).strftime("%b %d %H:%M")
		
	l = os.listdir(p)

	l.append('.')
	l.append('..')
	l = sorted(l, key = lambda s: re.sub('[^0-9a-zA-Z]+', '', s).lower())
	
	for file in l:
		f = os.stat(file)
		p = Path(file)
		print('{} {:>6} {:>15} {:>15} {:>15} {:>15}     {}'.format(stat.filemode(f.st_mode), f.st_nlink, p.owner(), p.group(), f.st_size, unix_datetime(), file))

run(str(p))
if len(sys.argv) > 2:
	for under_path in sorted(p.glob('*')):
		if (not os.path.isdir(str(under_path))) or (str(under_path).split('/')[-1][0] == '.'):
			continue
		print()
		print(str(under_path).split('/')[-1] + ':')
		run(str(under_path)) 