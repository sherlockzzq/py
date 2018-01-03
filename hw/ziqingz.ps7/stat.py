#!/usr/bin/env python3
import sys
import os
import stat
from pathlib import Path
import pytz
import time, datetime

def run(argv):

    if len(argv) == 1:
        print('stat: missing operand')
        print('Try \'stat --help\' for more information')
        return
    file = argv[1]

    if not os.path.exists(file):
        print('stat: cannot stat \'{}\': No such file or directory'.format(file))
        return

    def getmode(mode): #Reference: https://github.com/stvschmdt/Unix-Implementation-of-Stat/blob/master/mystat.c
        if stat.S_ISBLK(mode) != 0:
            return 'block device'
        elif stat.S_ISDIR(mode) != 0:
            return 'directory'
        elif stat.S_ISFIFO(mode) != 0:
            return 'FIFO/pipe'
        elif stat.S_ISLNK(mode) != 0:
            return 'symlink'
        elif stat.S_ISREG(mode) != 0:
            if os.stat(file).st_size == 0:
                return 'regular empty file'
            return 'regular file'
        elif stat.S_ISSOCK(mode) != 0:
            return 'socket'
        else:
            return 'unknown?'
    def gettime(t):
        return datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S.%f')

    st = os.stat(file)
    
    print('File: {}'.format(file))
    print('Size: {:<15}  Blocks: {:<10}IO Block: {} {}'.format(st.st_size, st.st_blocks, st.st_blksize, getmode(st.st_mode)))
    print('Divice: {}h:{}d   Inode: {:<10} Links: {}'.format(str(hex(st.st_dev))[-2:], st.st_dev, st.st_ino, st.st_nlink))
    print('Access: ({}/{}) Uid: ({}/{})    Gid: ({}/ {})'.format(str(oct(st.st_mode))[-4:], stat.filemode(st.st_mode), st.st_uid, Path(file).owner(), st.st_gid, Path(file).group()))
    print('Access: {} {}'.format(gettime(st.st_atime), time.strftime("%z", time.localtime()))) #Time Zone Reference: https://stackoverflow.com/questions/32353015/python-time-strftime-z-is-always-zero-instead-of-timezone-offset
    print('Modify: {} {}'.format(gettime(st.st_mtime), time.strftime("%z", time.localtime())))
    print('Change: {} {}'.format(gettime(st.st_ctime), time.strftime("%z", time.localtime())))
    print('Birth: -')

run(sys.argv)
