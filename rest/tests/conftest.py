
import pytest
from rest import create_app
from rest.models import db


@pytest.fixture
def app():

    app = create_app("test_config.py")

    with app.app_context():
        db.create_all()
    # get_db().executescript(_data_sql)

    # a simple page that says hello

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
