import pytest
from rest import create_app


@pytest.fixture()
def app():
    app = create_app("test_config.py")

    # other setup can go here

    yield app

    # clean up / reset resources here


def test_config():
    assert not create_app().testing
    assert create_app("test_config.py").testing


@pytest.fixture()
def client(app):
    @app.route("/hello")
    def hello_world():
        return "Hello, World!"
    return app.test_client()


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
