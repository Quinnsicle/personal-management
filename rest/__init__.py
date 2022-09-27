import os

from flask import Flask
from rest import crud, database
from rest.blueprints.api import Event
from rest.blueprints.api import Generic
from rest.models import Event as event_model


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "rest.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    database.init_db()

    app.register_blueprint(Event.api)
    app.register_blueprint(crud.bp)

    Generic.register_api(app, event_model, 'event')

    return app
