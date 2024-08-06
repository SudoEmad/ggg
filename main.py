import http.server
import socketserver

PORT = 8080

# Create a handler for the HTTP server
Handler = http.server.SimpleHTTPRequestHandler

# Create an HTTP server and bind it to the specified port
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving HTTP on port {PORT}")
    httpd.serve_forever()
