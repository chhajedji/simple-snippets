#!/usr/bin/env python2

"""
This example handles HTTP requests on port 6969. when requested path
is `/admin then we display given string and show request headers. For
any other, run simple http server.

Usage

Get your IP address with `ifconfig` and from your browser, go to
<ip_addres>/s:6969 and access your directory. Now go to
<ip_addres>/s:6969/admin to view other admin info.

"""

import SocketServer
import SimpleHTTPServer

# Subclass for SimpleHTTPServer.SimpleHTTPRequestHandler
class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/admin":
            self.wfile.write("Admin only page.")
            self.wfile.write(self.headers)

        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpServer = SocketServer.TCPServer(("", 6969), HttpRequestHandler)


httpServer.serve_forever()
