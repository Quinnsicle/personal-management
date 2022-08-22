import functools
from re import U
import json
import sqlite3
from werkzeug.exceptions import abort
from flask import (
    Blueprint,
    g,
    jsonify,
    request,
    render_template,
    redirect,
    url_for,
)
from flask.views import MethodView
from rest.api import *
bp = Blueprint("events", __name__, url_prefix="/api")


class Events(MethodView):

    def get(self):
        events = read_all_records()
        return json.dumps(events)

    def post(self):
        # create a new event
        pass

    def delete(self, event_id):
        # delete a single event
        pass

    def put(self, event_id):
        # update a single event
        pass

    class Year(MethodView):
        def get(self, year):
            events = read_all_records_within_year(year)
            return json.dumps(events)

    class Week(MethodView):
        def get(self, year, week):
            events = read_all_records_within_week(year, week)
            return json.dumps(events)


event_view = Events.as_view('events_api')
bp.add_url_rule('/events', view_func=event_view, methods=['GET',])
bp.add_url_rule('/', view_func=event_view, methods=['POST',])
bp.add_url_rule('/<int:event_id>', view_func=event_view,
                 methods=['GET', 'PUT', 'DELETE'])

year_view = Events.Year.as_view('events_year_api')
bp.add_url_rule('/events/year/<int:year>', defaults={'year': 2022},
                view_func=year_view, methods=['GET',])

week_view = Events.Week.as_view('events_week_api')
bp.add_url_rule('/events/year/<int:year>/week/<int:week>', 
                view_func=week_view, methods=['GET',])
