# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/6/21 20:48
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

data = {'err':0, 'msg':'OK'}
host = ('localhost',8080)

class Request(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

if __name__ == '__main__':
    server = HTTPServer(host, Request)
    print('Server is started! Listening at http://{}:{}'.format(host[0], host[1]))
    server.serve_forever()