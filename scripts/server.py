import http.server
import json,os

PORT = 8090

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        content = self.rfile.read(content_length)
        #data = json.loads(str(content))
        os.system(str(content)[2:-1])
        self.send_response(200)
        self.end_headers()

httpd = http.server.HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()