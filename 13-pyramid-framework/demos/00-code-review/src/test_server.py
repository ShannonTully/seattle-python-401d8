import requests


def test_server_sends_200_response():
    """test get 200 request"""
    response = requests.get('http://127.0.0.1:3000')
    assert response.status_code == 200


def test_server_sends_404_response():
    """test get 404 request"""
    response = requests.get('http://127.0.0.1:3000/not_a_thing')
    assert response.status_code == 404
    assert response.text == 'Not Found'


def test_server_sends_200():
    """test cowpay 200"""
    response = requests.get('http://127.0.0.1:3000/cowsay')
    assert response.status_code == 200
    assert response.text == '"messege about stuff"'


def test_server_sends_qs_response():
    """test get 200 dynamic"""
    response = requests.get('http://127.0.0.1:3000/cow?msg=meseegeback')
    assert response.status_code == 200
    assert response.text == '"meseegeback"'


def test_server_json():
    """test post 200 body and headers"""
    response = requests.post('http://127.0.0.1:3020/cow?msg=meseegeback')
    assert response.status_code == 200
    assert response.text == '"meseegeback"'
    assert response.headers['server'] == 'BaseHTTP/0.6 Python/3.6.4'


def test_server_get_endpoint_():
    '''Tests malformed query string GET'''
    res = requests.get('http://127.0.0.1:3000/cow?ms="wrong"')
    assert res.status_code == 400


def test_server_post_endpoint_400():
    '''Tests 400 post'''
    res = requests.post('http://127.0.0.1:3000/cow?ms="wrong"')
    assert res.status_code == 404


def test_server_json_():
    """test post 200 headers"""
    response = requests.post('http://127.0.0.1:3000/cow?msg=meseegeback')
    assert response.status_code == 200
    assert response.text == '"meseegeback"'
    assert response.headers['server'] == 'BaseHTTP/0.6 Python/3.6.4'
