import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Callable, Dict


class CustomHTTPServer(HTTPServer):

  def __init__(self, server_address, RequestHandlerClass, framework):
    super().__init__(server_address, RequestHandlerClass)
    self.framework = framework


class Reducelib:

  def __init__(self):
    self.routes: Dict[str, Callable[[], str]] = {}

  def render_template(self, path: str) -> str:
    try:
      with open(f'templates/{path}') as f:
        html = f.read()
    except FileNotFoundError:
      return f"{path} does not exist"
    return html

  def route(self, path: str):

    def wrapper(func: Callable[[], str]):
      self.routes[path] = func
      return func

    return wrapper

  def handle_request(self, path: str) -> str:
    if path in self.routes:
      func = self.routes[path]
      return func()  # Call the function to get the response
    else:
      return self.render_template(path[1:])  # Attempt to render a template

  def start(self, port: int = 8080):

    class RequestHandler(BaseHTTPRequestHandler):

      def do_GET(self):
        if self.path.startswith('/static/'):
          # Serve static files
          file_path = self.path[1:]  # Remove leading '/'
          if os.path.isfile(file_path):
            self.send_response(200)
            self.send_header("Content-type", "text/css")  # Default to CSS
            self.end_headers()
            with open(file_path, 'rb') as f:
              self.wfile.write(f.read())
          else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"File not found")
        else:
          response = self.server.framework.handle_request(self.path)
          if response.startswith("404 Not Found"):
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
          else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
          self.end_headers()
          self.wfile.write(response.encode())

    server = CustomHTTPServer(('localhost', port), RequestHandler, self)
    print(f"Starting server on port {port}")
    server.serve_forever()
