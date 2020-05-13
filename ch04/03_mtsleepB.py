# -*- conding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/10 20:00
使用线程和锁
"""

import _thread
from time import ctime, sleep

loops = [4, 2]
def loop(nloop, nsec, lock):
    print("strat loop {} at: {}".format(nloop, ctime()))
    sleep(nsec)
    print('loop {} done at: {}'.format(nloop, ctime()))
    lock.release()

def main():
    print('starting at: {}'.format(ctime()))
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        while locks[i].locked():
            pass
    print("all done at: {}".format(ctime()))

if __name__ == '__main__':
    main()
