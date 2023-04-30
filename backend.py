import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Extract the path from the request line
        request_path = self.path.split('?')[0]

        if request_path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello from the backend')
        elif request_path == '/admin/secret.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Oww you are of course an admin, so you can reach this place of the backend. Here is my secret: I love watching Peppa Pig such a good cartoon.')
        else:
            self.send_error(404, 'File Not Found')

# Create an HTTP server and listen for incoming requests
with socketserver.TCPServer(("", 80), MyHttpRequestHandler) as httpd:
    print("Server started on port 80...")
    httpd.serve_forever()
