# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/13 22:33
子类化的Thread
"""
import threading
from time import sleep, ctime

loops = [4, 2]
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    def run(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print('start loop {} at: {}'.format(nloop, ctime()))
    sleep(nsec)
    print('loop {} done at: {}'.format(nloop, ctime()))

def main():
    print('starting at:{}'.format(ctime()))
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
    print('all done at{}'.format(ctime()))

if __name__ == '__main__':
    main()