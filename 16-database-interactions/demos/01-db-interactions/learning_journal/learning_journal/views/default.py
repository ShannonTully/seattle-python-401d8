from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.view import view_config
from ..sample_data import MOCK_ENTRIES
from sqlalchemy.exc import DBAPIError
from ..models import Entry
from . import DB_ERR_MSG
import requests
import os


# https: // pixabay.com/api/docs/
API_KEY = os.environ.get('API_KEY', '')


@view_config(route_name='home', renderer='../templates/base.jinja2', request_method='GET')
def home_view(request):
    return {}


@view_config(route_name='auth', renderer='../templates/auth.jinja2')
def auth_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print('User: {}, Email: {}, Password(NEVER DO PLAIN TEXT PASSWORDS!): {}'.format(
            username, email, password))

        return HTTPFound(location=request.route_url('entries'))
    if request.method == 'GET':
        try:
            username = request.GET['username']
            password = request.GET['password']
            print('User: {}, Password(NEVER DO PLAIN TEXT PASSWORDS!): {}'.format(username, password))
            return HTTPFound(location=request.route_url('entries'))
        except KeyError:
            return {}
    return HTTPFound(location=request.route_url('home'))


@view_config(route_name='entries', renderer='../templates/entries.jinja2', request_method='GET')
def entries_view(request):
    try:
        query = request.dbsession.query(Entry)
        all_entries = query.all()
    except DBAPIError:
        return DBAPIError(DB_ERR_MSG, content_type='text/plain', status=500)

    return {'entries': all_entries}


@view_config(route_name='detail', renderer='../templates/detail.jinja2', request_method='GET')
def detail_view(request):
    try:
        entry_id = request.matchdict['id']
    except IndexError:
        return HTTPNotFound()

    try:
        query = request.dbsession.query(Entry)
        entry_detail = query.filter(Entry.id == entry_id).first()
    except DBAPIError:
        return DBAPIError(DB_ERR_MSG, content_type='text/plain', status=500)

    res = requests.get('https://pixabay.com/api?key={}&q={}'.format(
        API_KEY, entry_detail.title.split(' ')[0]))

    try:
        url = res.json()['hits'][0]['webformatURL']
    except (KeyError, IndexError):
        url = 'https://via.placeholder.com/300x300'

    return {
        "entry": entry_detail,
        "img": url,
    }


@view_config(route_name='new', renderer='../templates/new.jinja2')
def new_view(request):
    if request.method == 'POST':
        request.response.status = 201
        return HTTPFound(location=request.route_url('entries'))
    if request.method == 'GET':
        return {}
