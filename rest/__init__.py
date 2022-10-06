import os

from flask import Flask
from rest import crud
from rest.blueprints.api import Event
from rest.blueprints.api import Generic
from rest.models import Event as event_model


def create_app(config_file="config.py"):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile(config_file, silent=False)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from rest.models import db
    db.init_app(app)

    with app.app_context():
        db.create_all()
        # event = event_model('name', '2022-10-31T01:30:00.000-05:00',
        #                     '2022-10-31T01:35:00.000-05:00', None, None, 'test')
        # db.session.add(event)
        db.session.commit()

    app.register_blueprint(Event.api)
    app.register_blueprint(crud.bp)
    Generic.register_api(app, event_model, 'event')

    return app


app = create_app()
