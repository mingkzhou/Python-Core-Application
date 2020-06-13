# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/6/7 11:16
"""
from multiprocessing import Process
import os
from time import sleep

def run_proc(name, age, **kwargs):
    for i in range(10):
        print('子进程运行中，name={}, age={}, pid={}'.format(name, age, os.getpid()))
        print(kwargs)
        sleep(0.5)
if __name__=='__main__':
    print('父进程{}'.format(os.getppid()))
    p = Process(target=run_proc, args=('test', 18), kwargs={'m':2})
    print('子进程将要执行')
    p.start()
    sleep(1)
    p.terminate()
    p.join()
    print('子进程已经结束')
