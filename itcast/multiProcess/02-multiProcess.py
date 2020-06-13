# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/6/7 10:24
"""
import os
import time
pid = os.fork()

# if pid == 0:
#     print('haha 1')
# else:
#     print('haha 2')

# getpid(), getppid()
# if pid < 0:
#     print('fork 调用失败')
# elif pid == 0:
#     print('子进程{}, 父进程{}'.format(os.getpid(), os.getppid()))
# else:
#     print('父进程{},子进程{}'.format(os.getpid(), os.getppid()))

# 多进程中，每个进程中所有数据（包括全局变量）都各有一份，互不影响
num = 0
if pid == 0:
    num += 1
    print('haha1 num={}'.format(num))
else:
    time.sleep(1)
    num += 1
    print('haha2 num={}'.format(num))
