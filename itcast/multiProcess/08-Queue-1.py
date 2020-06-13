# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/6/13 10:42
"""

from multiprocessing import Queue

q = Queue(3)
q.put('1')
q.put('2')
print(q.full())
q.put('3')
print(q.full())

try:
    q.put('4', True, 2)
except:
    print('消息队列已满，现有数量:{}'.format(q.qsize()))
try:
    q.put_nowait('4')
except:
    print('消息队列已满，现有数量:{}'.format(q.qsize()))

