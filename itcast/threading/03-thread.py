# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/6/14 14:53
"""

import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = 'I`m ' + self.name + ' @ ' + str(i)
            print(msg)
if __name__ == '__main__':
    for i in range(5):
        t = MyThread()
        t.start()
