# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/7/5 11:43
"""
from socket import *

# 创建套接字
tcpSerSocket = socket(AF_INET, SOCK_STREAM)
# 绑定本地信息
address = ('', 7788)
tcpSerSocket.bind(address)
# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动
tcpSerSocket.listen(5)
# 如果有新的客户端来链接服务器， 那么就产⽣⼀个新的套接字专⻔为这个客户端服务器
# newSocket⽤来为这个客户端服务
# tcpSerSocket就可以省下来专⻔等待其他新客户端的链接
newSocket, clientAddr = tcpSerSocket.accept()
# 接收对方发送过来的数据，最大接收1024字节
recvData = newSocket.recv(1024)
print('接收到的数据{}'.format(recvData.decode('utf-8')))
# 发送一些数据到客户端
newSocket.send('thank you')
newSocket.close()
tcpSerSocket.close()
