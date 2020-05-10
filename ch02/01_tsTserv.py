# -*- conding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/8 22:32
TCP服务器
"""

from socket import *
from time import ctime

# 空白表示可以使用任意地址
HOST = ''
PORT = 21567
# 缓冲区大小为1kb
BUFSIZ = 1024
ADDR = (HOST, PORT)

# AF_INET 基于网络的套接字, SOCK_STREAM:tcp, SOCK_DGRAM:udp
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
# 最大连接数为5
tcpSerSock.listen(5)

while True:
    print('waiting for connecting...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:{}'.format(addr))

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'),
                                     bytes(data, 'utf-8')))
    tcpCliSock.close()

tcpSerSock.close()