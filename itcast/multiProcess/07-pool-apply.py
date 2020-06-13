# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/6/13 10:31
"""
from multiprocessing import Pool
import os, time, random

def worker(msg):
    start = time.time()
    print('{}开始执行，进程号为{}'.format(msg, os.getpid()))
    time.sleep(random.random()*2)
    stop = time.time()
    print('{},执行完毕，耗时{:0.2f}'.format(msg, (stop-start)))

pool = Pool(3)
for i in range(0, 10):
    pool.apply(worker, (i,))
print('---start---')
pool.close()
pool.join()
print('---end---')