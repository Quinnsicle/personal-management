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
        year = request.args.get('year')
        week = request.args.get('week')
        if year and week:
            print(week)
            return json.dumps(read_all_records_within_week(year, week))
        if year:
            print(year)
            return json.dumps(read_all_records_within_year(year))
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


event_view = Events.as_view('events_api')
bp.add_url_rule('/events', view_func=event_view, methods=['GET',])
bp.add_url_rule('/', view_func=event_view, methods=['POST',])
bp.add_url_rule('/<int:event_id>', view_func=event_view,
                 methods=['GET', 'PUT', 'DELETE'])
