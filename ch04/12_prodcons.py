# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/16 11:33
生产者消费者问题
"""
from random import randint
from time import sleep
from queue import Queue
from ch04.myThread import MyThread

def writeQ(queue):
    print("producing object for Q...")
    queue.put('xxx', 1)
    print('size now {}'.format(queue.qsize()))

def readQ(queue):
    val = queue.get(1)
    print('consumed object from Q... size now {}'.format(queue.qsize()))

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(1, 3))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2, 5)
    q = Queue(32)
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
    print("all done")

if __name__ == '__main__':
    main()