# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/6/25 11:17
"""

import socket
from multiprocessing import Process
import re

def handleClient(clientSocket):
    recvData = clientSocket.recv(2014)
    requestHeaderLines = recvData.splitlines()
    for line in requestHeaderLines:
        print(line)

    httpRequestMethodLine = requestHeaderLines[0].decode('utf-8')
    getFileName = re.match(r'[^/]+(/[^ ]*)', httpRequestMethodLine).group()
    print('file name is ===>{}'.format(getFileName))
    if getFileName == '/':
         getFileName = documentRoot + '/index.html'
    else:
        getFileName = documentRoot + '/index.html'
    print('file name is ===2>{}'.format(getFileName))

    try:
        f = open(getFileName)
    except IOError:
        responseHeaderLines = "HTTP/1.1 404 not found\r\n"
        responseHeaderLines += "\r\n"
        responseBody = "====sorry ,file not found===="
    else:
        responseHeaderLines = "HTTP/1.1 200 OK\r\n"
        responseHeaderLines += "\r\n"
        responseBody = f.read()
        f.close()
    finally:
        response = responseHeaderLines + responseBody
        clientSocket.send(bytes(response, 'utf-8'))
        clientSocket.close()

def main():
    '作为程序的主控制⼊⼝'
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind(("", 7788))
    serverSocket.listen(10)
    while True:
        clientSocket,clientAddr = serverSocket.accept()
        clientP = Process(target = handleClient, args = (clientSocket,))
        clientP.start()
        clientSocket.close()

documentRoot = './html'

if __name__ == "__main__":
    main()