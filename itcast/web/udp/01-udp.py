# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/7/5 10:55
"""

from socket import *

# 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)
# 准备接收方的地址
sendAddr = ('192.168.1.103', 8080)
# 从键盘获取数据
sendData = input('请输入发送的数据:')
# 发送数据到指定电脑上
udpSocket.sendto(sendData.encode('utf-8'), sendAddr)
# 等待接收对方发送的数据
recvData = udpSocket.recvfrom(1024)
# 关闭套接字
udpSocket.close()