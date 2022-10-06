from rest import create_app


def test_config():
    assert not create_app().testing
    assert create_app("test_config.py").testing


def test_hello(client):
    response = client.get('/hello')
    assert b'Hello, World!' in response.data
