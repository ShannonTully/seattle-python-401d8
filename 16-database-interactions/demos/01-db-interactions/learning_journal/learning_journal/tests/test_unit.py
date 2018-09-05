

def test_default_response_home_view(dummy_request):
    from ..views.default import home_view

    response = home_view(dummy_request)
    assert len(response) == 0
    assert type(response) == dict


def test_default_response_entries_view(dummy_request):
    from ..views.default import entries_view

    response = entries_view(dummy_request)
    assert len(response) == 1
    assert isinstance(response, dict)


def test_default_response_new_view(dummy_request):
    from ..views.default import new_view

    response = new_view(dummy_request)
    assert len(response) == 0
    assert type(response) == dict
