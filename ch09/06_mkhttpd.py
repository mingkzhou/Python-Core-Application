# -*- coding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/30 18:53
简单的web服务器
python2 中BaseHTTPServer,SampleHTTPServer,CGIHTTPServer模块在python3中合并到http.client中
"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            f = open(self.path[1:], 'r')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
        except IOError:
            self.send_error(404, 'File Not Found: {}'.format(self.path))

def main():
    try:
        server = HTTPServer(('', 80), MyHandler)
        print('Welcome to the machine...')
        print('Press ^C once or twice to quit.')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shuuting down server')
        server.socket.close()

if __name__ == "__main__":
    main()
