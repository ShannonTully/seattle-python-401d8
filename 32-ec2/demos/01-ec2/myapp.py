# -*- coding: utf-8 -*-
"""A simple WSGI app for deployment."""
from sys import version_info


def app(environ, start_response):
    """A simple WSGI app."""
    data = "Hello, World!\n"

    if version_info.major > 2:
        data = data.encode("utf-8")

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return [data]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, app)
    srv.serve_forever()
