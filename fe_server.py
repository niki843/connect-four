import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

Handler.extensions_map = {
		'.html': 'text/html',
		'.png': 'image/png',
		'.jpg': 'image/jpg',
		'.svg':	'image/svg+xml',
		'.css':	'text/css',
		'.js':	'application/x-javascript',
		'': 'application/octet-stream', # Default
}

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
