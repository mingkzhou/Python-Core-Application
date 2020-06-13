# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/6/7 11:01
"""
import os
from multiprocessing import Process

# 子进程要执行的代码
def run_proc(name):
    print('子进程运行中，name={},pid={}'.format(name, os.getpid()))

if __name__ == '__main__':
    print('父进程 {}'.format(os.getppid()))
    p = Process(target=run_proc, args=('test', ))
    print('子进程将要执行')
    p.start()
    p.join()
    print('子进程已经结束')