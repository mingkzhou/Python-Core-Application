# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/10 15:06
Twisted Reactor TCP客户端
"""

from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21567

class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = input('> ')
        if data:
            print('...sending {}...'.format(data))
            self.transport.write(data.encode('utf-8'))
        else:
            self.transport.loseConnection()
    def connectionMade(self):
        self.sendData()
    def dataReceived(self, data):
        print(data)
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason:reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()