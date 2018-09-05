from pyramid.view import view_config
from pyramid.response import Response
from ..sample_data import MOCK_ENTRIES
from pyramid.httpexceptions import HTTPFound, HTTPNotFound


@view_config(
    route_name='home',
    renderer='../templates/base.jinja2',
    request_method='GET')
def home_view(request):
    return Response('I did a thing')


@view_config(
    route_name='auth',
    renderer='../templates/auth.jinja2')
def auth_view(request):
    if request.method == 'GET':
        try:
            username = request.GET['username']
            password = request.GET['password']
            print('User: {}, Pass: {}'.format(username, password))

            return HTTPFound(location=request.route_url('entries'))

        except KeyError:
            return {}

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print('User: {}, Pass: {}, Email: {}'.format(username, password, email))

        return HTTPFound(location=request.route_url('entries'))

    return HTTPNotFound()


@view_config(
    route_name='detail',
    renderer='../templates/detail.jinja2',
    request_method='GET')
def detail_view(request):
    return {}


@view_config(
    route_name='entries',
    renderer='../templates/entries.jinja2',
    request_method='GET')
def entries_view(request):
    from random import randint

    return {
        'entries': MOCK_ENTRIES,  # 'entries' is the reference we use in the template
        'message': 'Hello world',
        'rand': randint(0, 10)}


@view_config(
    route_name='new',
    renderer='../templates/new.jinja2',
    request_method='GET')
def new_view(request):
    return {}


