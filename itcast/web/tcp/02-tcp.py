# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/7/5 11:52
"""
from socket import *
# 创建socket
tcpClientSocket = socket(AF_INET, SOCK_STREAM)
# 连接服务器
serAddr = ('192.168.1.102', 7788)
tcpClientSocket.connect(serAddr)
# 提示⽤户输⼊数据
sendData = input("请输入要发送的数据")
tcpClientSocket.send(sendData.encode('utf-8'))
recvData = tcpClientSocket.recv(1024)
print('接收到的数据{}'.format(recvData.decode('utf-8')))
tcpClientSocket.close()