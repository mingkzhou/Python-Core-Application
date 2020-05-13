# -*- conding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/12 22:56
使用threading模块
"""

import threading
from time import ctime, sleep

loops = [4, 2]
def loop(nloop, nsec):
    print('start loop {} at: {}'.format(nloop, ctime()))
    sleep(nsec)
    print('loop {} done at: {}'.format(nloop, ctime()))

def main():
    print('starting at:{}'.format(ctime()))
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
    print('all done at{}'.format(ctime()))

if __name__ == '__main__':
    main()