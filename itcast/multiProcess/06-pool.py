# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/6/7 16:21
"""

from multiprocessing import Pool
import os
import random
import time

def worker(msg):
    t_start = time.time()
    print('{}开始执行，进程号{}'.format(msg, os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print('{}执行完毕，耗时{:.2f}'.format(msg, (t_stop-t_start)))

po = Pool(3)
for i in range(0,10):
    po.apply_async(worker, (i,))
print('----start----')
po.close()
po.join()
print('----end----')