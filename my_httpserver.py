#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os

SCRIPT_FOLDER = os.path.dirname(os.path.realpath(__file__)) + '/'

# Create custom HTTPRequestHandler class
class myHTTPRequestHandler(BaseHTTPRequestHandler):

    # handle GET command
    def do_GET(self):

        try:
            if self.path.endswith('.html'):
                f = open(SCRIPT_FOLDER + self.path)  # open requested file

                # send code 200 response
                self.send_response(200)

                # send header first
                self.send_header('Content-type', 'text-html')
                self.end_headers()

                # send file content to client
                self.wfile.write(f.read())
                f.close()
                return

        except IOError:
            self.send_error(404, 'file not found')


def run():
    print('http server is starting...')

    # ip and port of server
    # by default http server port is 80
    server_address = ('192.168.0.176', 8080)
    httpd = HTTPServer(server_address, myHTTPRequestHandler)
    print('http server is running...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
