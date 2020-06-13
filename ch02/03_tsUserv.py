# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/10 13:15
UDP服务器
"""

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)
while True:
    print("waiting for message...")
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s] %s'%(ctime(), bytes(data, 'utf-8')), addr)
    print("...received from and returned to: {}".format(addr))

udpSerSock.close()