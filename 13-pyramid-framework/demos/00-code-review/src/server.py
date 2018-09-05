from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
# import sys
from cowpy import cow

# http://amazon.com/cat/books?name='Frank Herbert'&genre='SciFi'&....
# self.path = /cat/books?name='Frank Herbert'&genre='SciFi'&....
# query_string = name='Frank Herbert'&genre='SciFi'&....


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        print(parsed_path)
        # parsed_path = Parsed_Path(path='/cat/books', query='name='Frank Herbert'&genre='SciFi'&....')
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            # Set Headers
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            # Set Body
            self.wfile.write(b'''
                <!DOCTYPE html>
                <html>
                <head>
                    <title> cowsay </title>
                </head>
                <body>
                    <header>
                        <nav>
                        <ul>
                            <li><a href="/cowsay">cowsay</a></li>
                        </ul>
                        </nav>
                    <header>
                    <main>
                    <p>Project description</p>
                    <p>a socket client that sends a properly-formatted HTTP request,
                    and a server that parses a properly-formatted HTTP request
                    and returns a properly-formatted HTTP response</p>
                    </main>
                </body>
                </html>
                ''')


        elif parsed_path.path == '/cowsay':
            cheese = cow.Moose(tongue=True)
            msg = cheese.milk("message about stuff")

            self.send_response(200)
            self.end_headers()
            self.wfile.write(msg.encode('utf8'))

        elif parsed_path.path == '/cow':
            # import pdb; pdb.set_trace()
            try:
                cat = parsed_qs['msg'][0]
            except KeyError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'something is broken')
                return
            cheese = cow.Moose(tongue=True)
            msg = cheese.milk(cat)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(msg.encode('utf8'))

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_POST(self):
        parsed_path = urlparse(self.path)
        # parsed_qs = parse_qs(parsed_path.query)
        if parsed_path.path == '/cow':
            try:
                content_length = int(self.headers['Content-Length'])
                body = json.loads(self.rfile.read(content_length).decode('utf8'))
                # import pdb; pdb.set_trace()
            except KeyError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'something is broken')
                return
            cheese = cow.Moose(tongue=True)
            msg = cheese.milk(body['msg'])

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'content': msg}).encode('utf8'))
            return
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')


def create_server():
    return HTTPServer(('127.0.0.1', 3000), SimpleHTTPRequestHandler)


def run_forever():
    server = create_server()

    try:
        print('Starting server on port 3000')
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run_forever()
