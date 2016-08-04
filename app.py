#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 解决py2.7中文出现write错误的问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 解决py2.7中文出现write错误的问题 #

# 从wsgiref模块导入:
from wsgiref.simple_server import make_server, WSGIServer, WSGIRequestHandler, ServerHandler
from processPool.PooledProcessMixIn import PooledProcessMixIn
from threading import Thread
import os
from project import app
from project.bottle import debug, run

debug(True)


# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
def start_httpd(host, port):
    global httpd_server

    class ProcessPoolWSGIServer(PooledProcessMixIn, WSGIServer):
        pass

        def finish_request(self, request, client_address):
            try:
                WSGIServer.finish_request(self, request, client_address)
            except IOError as ex:
                if ex.errno == 32:
                    print('client disconnected.')
                else:
                    raise ex

    class FixedServerHandler(ServerHandler):
        def finish_response(self):
            try:
                ServerHandler.finish_response(self)
            except IOError as ex:
                if ex.errno == 32:
                    print('client disconnected.')
                else:
                    raise ex

    class FixedWSGIRequestHandler(WSGIRequestHandler):
        def handle(self):
            """Handle a single HTTP request"""
            self.raw_requestline = self.rfile.readline(65537)
            if len(self.raw_requestline) > 65536:
                self.requestline = ''
                self.request_version = ''
                self.command = ''
                self.send_error(414)
                return

            if not self.parse_request():  # An error code has been sent, just exit
                return

            handler = FixedServerHandler(
                self.rfile, self.wfile, self.get_stderr(), self.get_environ()
            )
            handler.request_handler = self  # backpointer for logging
            handler.run(self.server.get_app())

    httpd_server = make_server(host, port, app, server_class=ProcessPoolWSGIServer,
                               handler_class=FixedWSGIRequestHandler)
    th = Thread(target=httpd_server.serve_forever)
    th.setDaemon(True)
    th.start()
    print('Started httpd %s' % port)
    th.join()
    # try:
    #     while th.isAlive():
    #         pass
    # except KeyboardInterrupt:
    #     print('stopped by keyboard')



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    start_httpd("0.0.0.0", 8000)
    # run(app, reloader=True, interval=1, host='0.0.0.0', port=port)
