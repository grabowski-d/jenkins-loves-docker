import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
import os


class GreetingsGenerator:
    def __init__(self, query_components):
        if 'name' in query_components:
            self._name = query_components["name"][0]
        else:
            self._name = "world"

    def generate(self):
        return "hello " + self._name


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        generator = GreetingsGenerator(parse_qs(urlparse(self.path).query))
        html = f"<html><head></head><body><h1>{generator.generate()}</h1></body></html>"

        self.wfile.write(bytes(html, "utf8"))
        return


if __name__ == '__main__':
    handler_object = MyHttpRequestHandler
    PORT = int(os.getenv('SERVER_PORT', '8000'))

    my_server = socketserver.TCPServer(("", PORT), handler_object)
    print("Starting server...")
    my_server.serve_forever()
