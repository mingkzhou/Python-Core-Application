# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/10 14:10
SocketServer TCP客户端
"""
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input("> ")
    if not data:
        break
    tcpCliSock.send('{}\r\n'.format(data))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.strip())
tcpCliSock.close()