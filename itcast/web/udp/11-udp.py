# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/7/5 10:45
"""

import socket, sys

dest = ('<broadcast>', 7788)

# 创建udp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 最这个需要发送广播数据的套接字进行修改设置，否则不能发送广播数据
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# 以广播的形式发送数据到本网络的所有电脑中
s.sendto('hi'.encode('utf-8'), dest)
print("等待对方回复")
while True:
    (buf, address) = s.recvfrom(2048)
    print('received from {}: {}'.format(address, buf))
