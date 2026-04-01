import os, sys
os.chdir('/Users/Paul/Desktop/Projets Dev/Mitmi')
import http.server, socketserver

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass

with socketserver.TCPServer(("", 3456), Handler) as httpd:
    httpd.serve_forever()
