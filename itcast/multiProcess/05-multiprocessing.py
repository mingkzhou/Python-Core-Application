# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/6/7 11:34
"""
from multiprocessing import Process
import time
import os

# 继承Process类
class Process_class(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval
    # 重写Process类的run方法
    def run(self):
        print('子进程{}开始执行，父进程为{}'.format(os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_stop = time.time()
        print('执行结束，耗时{:.2f}'.format(os.getpid(), t_stop-t_start))

if __name__ == '__main__':
    t_start = time.time()
    print('当前程序进程{}'.format(os.getpid()))
    p1 = Process_class(2)
    p1.start()
    p1.join()
    t_stop = time.time()
    print('{}执行结束，耗时{:.2f}'.format(os.getpid(), t_stop-t_start))