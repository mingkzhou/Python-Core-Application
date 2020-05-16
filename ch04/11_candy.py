# -*- conding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/16 11:11
糖果机和信号量
"""

from atexit import register
from random import randrange
from threading import Thread, Lock, BoundedSemaphore
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)
def refill():
    lock.acquire()
    print('Refilling candy...')
    try:
        candytray.release()
    except ValueError:
        print('full, skipping')
    else:
        print('OK')
    lock.release()

def buy():
    lock.acquire()
    print('buying candy...')
    # 检测是否所有资源都已经消费完
    if candytray.acquire(False):
        print('OK')
    else:
        print('empty, skiping')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

def main():
    print('starting at: {}'.format(ctime()))
    nloops = randrange(2, 6)
    print('the candy machine full with {} bars'.format(MAX))
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2), )).start()
    Thread(target=producer, args=(nloops, )).start()

@register
def _atexit():
    print('all done at {}'.format(ctime()))

if __name__ == '__main__':
    main()
