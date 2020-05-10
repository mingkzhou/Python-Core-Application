# -*- conding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/10 14:37
twisted reactor TCP服务器
"""
from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from: {}'.format(clnt))
    def dataReceived(self, data):
        self.transport.write('[{}] {}'.format(ctime(), data.decode('utf-8')))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection ...')
reactor.listenTCP(PORT, factory)
reactor.run()