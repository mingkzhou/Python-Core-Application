# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/10 13:57
SocketServer TCP服务器
"""

from socketserver import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handler(self):
        print("...connected from: {}".format(self.client_address))
        self.wfile.write('[{}] {}'.format(ctime(), self.rfile.readline()))

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()