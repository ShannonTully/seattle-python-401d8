import pytest
from pyramid import testing


@pytest.fixture
def dummy_request(scope='session'):
    """Create a dummy GET request with a dbsession."""
    return testing.DummyRequest()
