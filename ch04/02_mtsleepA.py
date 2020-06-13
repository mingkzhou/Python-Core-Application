# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/10 17:30
使用thread模块
"""
import _thread
from time import sleep, ctime

def loop0():
    print('start loop 0 at: {}'.format(ctime()))
    sleep(4)
    print('loop 0 done at: {}'.format(ctime()))

def loop1():
    print('start loop 1 at: {}'.format(ctime()))
    sleep(2)
    print('loop 1 done at: {}'.format(ctime()))
def main():
    print('starting at: {}'.format(ctime()))
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    # 等待子线程执行完
    sleep(6)
    print('all done at: {}'.format(ctime()))

if __name__ == '__main__':
    main()