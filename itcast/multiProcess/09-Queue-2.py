# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/6/13 11:08
"""
from multiprocessing import Process, Queue
import os, time, random

# 写入数据进程执行代码
def write(q):
    for value in ['A', 'B', 'C']:
        print('put {} to queue'.format(value))
        q.put(value, False)
        time.sleep(random.random())
def read(q):
    while True:
        if not q.empty():
            value = q.get(False)
            print('get {} from queue'.format(value))
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':
    # 会阻塞
    q = Queue(2)
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))
    # 启动子进程pw，写入
    pw.start()
    # 等待pw结束
    pw.join()
    pr.start()
    pr.join()
    print('所有数据都写入并且读完')