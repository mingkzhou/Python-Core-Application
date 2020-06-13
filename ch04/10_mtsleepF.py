# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/16 10:52
锁和更多的随机性
"""
from atexit import register
from random import randrange
from threading import Lock, Thread, currentThread
from time import ctime, sleep

class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)
lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()

def loop(nsec):
    myname = currentThread().name
    lock.acquire()
    remaining.add(myname)
    print('{} started {}'.format(ctime(), myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print('{} completed {} {}'.format(ctime(), myname, nsec))
    print('remaining {}'.format(remaining or 'None'))
    lock.release()

def main():
    for pause in loops:
        Thread(target=loop, args=(pause, )).start()

@register
def _atexit():
    print('all done at {}'.format(ctime()))

if __name__ == '__main__':
    main()