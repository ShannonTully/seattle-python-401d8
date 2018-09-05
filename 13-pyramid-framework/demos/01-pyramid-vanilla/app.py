from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse


def basic_view(request):
    """Basic home view which sends a 200 OK Response"""
    return Response('Hello World')


def json_view(request):
    return {'content': 'Hello World'}


def html_view(request):
    return FileResponse('./base.html', content_type='text/html')


if __name__ == '__main__':
    # Set up a config object to work with
    config = Configurator()

    # Define Routes
    config.add_route('basic', '/')
    config.add_route('json', '/json')
    config.add_route('html', '/html')

    # Define Views
    config.add_view(basic_view, route_name='basic')
    config.add_view(json_view, route_name='json', renderer='json')
    config.add_view(html_view, route_name='html')

    # Create an WSGI instance
    app = config.make_wsgi_app()

    # Configure our Server instance
    server = make_server('0.0.0.0', 6543, app)

    # Tell the server to start and run forever
    server.serve_forever()
