# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/14 22:26
斐波那契数列、阶乘与累加
"""
from ch04.myThread import MyThread
from time import ctime, sleep

def fib(x):
    sleep(0.005)
    if x<2:
        return 1
    return fib(x-2) + fib(x-1)

def fac(x):
    sleep(0.1)
    if x<2:
        return 1
    return fac(x-1)*x

def sum(x):
    sleep(0.1)
    if x<2:
        return x
    return x+sum(x-1)

funcs = [fib, fac, sum]
n=12
def main():
    nfuncs = range(len(funcs))
    print('***** SINGLE THREAD')
    for i in nfuncs:
        print('starting {} at {}'.format(funcs[i].__name__, ctime()))
        print(funcs[i](n))
        print('{} finished at: {}'.format(funcs[i].__name__, ctime()))
    print('***** MULTIPLE THREADS')
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n, ), funcs[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())
    print('all done')

if __name__ == '__main__':
    main()
