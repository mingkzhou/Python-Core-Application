# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/6/13 11:21
进程池中都Queue
"""

from multiprocessing import Manager, Pool
import os, time, random

def reader(q):
    print('reader 启动{}, 父进程为{}'.format(os.getpid(), os.getppid()))
    for i in range(q.size()):
        print('reader从Queue获取消息{}'.format(q.get(True)))
def writer(q):
    print('writer启动{}，父进程为{}'.format(os.getpid(), os.getppid()))
    for i in 'dog':
        q.put(i)

if __name__ == '__main__':
    print('{}start'.format(os.getpid()))
    q = Manager().Queue()
    po = Pool()
    po.apply(writer, (q, ))
    po.apply(reader, (q))
    po.close()
    po.join()
    print('{} end'.format(os.getpid()))