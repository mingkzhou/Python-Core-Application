# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/6/14 13:59
"""

import threading
import time

def sing():
    for i in range(3):
        print('正在唱歌{}'.format(i))
        time.sleep(1)

def dance():
    for i in range(3):
        print('正在跳舞{}\n'.format(i))
        time.sleep(1)

if __name__ == '__main__':
    print('=====start=====')
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    print('=====end=====')

    while True:
        length = len(threading.enumerate())
        print('当前运行的线程数为{}'.format(length))
        if length<=1:
            break
        time.sleep(1)