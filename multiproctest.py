#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2011.03.21
# 2011.08.24

from multiprocessing import Process
import time

def func(num):
    print 'Loop', num
    time.sleep(num+1)
    print 'Loop %d done sleeping' % num

if __name__ == '__main__':
    for num in range(5):
        p = Process(target=func, args=(num,))
        p.start()