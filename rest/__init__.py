import os

from flask import Flask
from rest import crud
from rest import database
from rest.blueprints.api import Event
from rest.blueprints.api import Generic
from rest.models import Event as event_model


class Config(object):
    """Base config, uses staging database server."""
    TESTING = False
    DB_SERVER = ''

    @property
    def DATABASE_URI(self):  # Note: all caps
        return f"mysql://user@{self.DB_SERVER}/foo"


class ProductionConfig(Config):
    """Uses production database server."""
    DB_SERVER = ''


class DevelopmentConfig(Config):
    SECRET_KEY = "dev",
    DB_SERVER = 'localhost'
    #     DATABASE=os.path.join(app.instance_path, "rest.sqlite"),


class TestingConfig(Config):
    TESTING = True
    DB_SERVER = 'localhost'
    DATABASE_URI = 'sqlite:////tmp/test.db'


def create_app(config_file="config.py"):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile(config_file, silent=False)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    database.init_db(app.config["DATABASE_URI"])

    app.register_blueprint(Event.api)
    app.register_blueprint(crud.bp)

    Generic.register_api(app, event_model, 'event')

    return app
