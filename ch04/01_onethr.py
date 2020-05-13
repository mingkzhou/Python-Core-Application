# -*- conding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/10 17:24
使用单线程执行循环
"""

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
    loop0()
    loop1()
    print('all done at: {}'.format(ctime()))

if __name__ == '__main__':
    main()
