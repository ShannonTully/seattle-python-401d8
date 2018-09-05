from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/base.jinja2', request_method='GET')
def get_home_view(request):
    return {}


@view_config(route_name='auth', renderer='../templates/auth.jinja2', request_method='GET')
def get_auth_view(request):
    return {}


@view_config(route_name='entries', renderer='../templates/entries.jinja2', request_method='GET')
def get_entries_view(request):
    return {}


@view_config(route_name='detail', renderer='../templates/detail.jinja2', request_method='GET')
def get_detail_view(request):
    return {}


@view_config(route_name='new', renderer='../templates/new.jinja2', request_method='GET')
def get_new_view(request):
    return {}
