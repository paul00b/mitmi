import os, sys
os.chdir('/Users/Paul/Desktop/Projets Dev/Mitmi')
import http.server, socketserver

PORT = int(os.environ.get('PORT', 3456))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
