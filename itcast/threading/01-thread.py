# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/6/14 13:56
"""
import threading
import time

def saySorry():
    print('111')
    time.sleep(1)
if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=saySorry)
        # 创建好的线程，使用start()来启动
        t.start()