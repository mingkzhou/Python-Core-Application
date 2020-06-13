# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/13 22:38
Thread子类
"""
import threading
from time import sleep, ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        print('starting {} at {}'.format(self.name, ctime()))
        self.res = self.func(*self.args)
        print('{} finished at {}'.format(self.name, ctime()))

    def getResult(self):
        return self.res