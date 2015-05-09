import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import scrape
import query


class Server:
    def __init__(self):
        HandlerClass = SimpleHTTPRequestHandler
        ServerClass  = BaseHTTPServer.HTTPServer
        Protocol     = "HTTP/1.0"

        server_address = ('127.0.0.1', 8000)

        print 'Creating a server...'
        HandlerClass.protocol_version = Protocol
        self._server = ServerClass(server_address, HandlerClass)
        print '...done'
        
        self._posts_per_store = scrape.get_all_posts()

    def run():
        sa = self._server.socket.getsockname()
        print "Serving HTTP on", sa[0], "port", sa[1], "..."
        
        self._server.serve_forever()
