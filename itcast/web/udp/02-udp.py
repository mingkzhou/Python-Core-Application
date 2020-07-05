# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/7/5 11:10
"""
from socket import *
from time import ctime

# 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)
# 绑定本地的相关信息
bindAddr = ('', 7788)
udpSocket.bind(bindAddr)
while True:
    # 等待接收对方发送的数据
    recvData = udpSocket.recvfrom(1024)
    print('{} {}: {}'.format(ctime(), recvData[1][0], recvData[0]))
udpSocket.close()