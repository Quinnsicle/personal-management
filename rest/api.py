import csv
import io
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
from rest.models import Event
from rest.dal.event import *
from flask_sqlalchemy import *

bp = Blueprint("api", __name__, url_prefix="/api")



class Events(MethodView):
    @staticmethod
    def output_format(events: list, format: str = "json"):
        if format == "csv":
            csv_out = io.StringIO()
            
            keys = Event.__table__.columns.keys()

            writer = csv.writer(csv_out, keys)
            writer.writerow(keys)
            for event in events:
                writer.writerow([event.name, 
                                 event.start_date_time, 
                                 event.end_date_time, 
                                 event.category,
                                 event.tags,
                                 event.author_id])

            return csv_out.getvalue()

        if format == "json":
            return jsonify(events)

        return "sorry, this api doesn't support " + format

    def get(self):
        year = request.args.get("year")
        week = request.args.get("week")
        format = request.args.get("format")
        if format is None:
            format = "json"
        if year and week:
            year_week = "{}-W{}".format(year, week)
            start_date = datetime.datetime.strptime(year_week + "-1", "%Y-W%W-%w").strftime("%Y-%m-%d")
            end_date = datetime.datetime.strptime(year_week + "-0", "%Y-W%W-%w").strftime("%Y-%m-%d")
            return self.output_format(Event.query.filter(Event.start_date_time.between(start_date, end_date)).all(), format)
        if year:
            start_date = "{}-01-01".format(year)
            end_date = "{}-12-31".format(year)
            return self.output_format(Event.query.filter(Event.start_date_time.between(start_date, end_date)).all(), format)

        return self.output_format(Event.query.all(), format)

    def post(self):
        # create a new event
        pass

    def delete(self, event_id):
        # delete a single event
        pass

    def put(self, event_id):
        # update a single event
        pass


event_view = Events.as_view("events_api")
bp.add_url_rule(
    "/events",
    view_func=event_view,
    methods=[
        "GET",
    ],
)
bp.add_url_rule(
    "/",
    view_func=event_view,
    methods=[
        "POST",
    ],
)
bp.add_url_rule(
    "/<int:event_id>", view_func=event_view, methods=["GET", "PUT", "DELETE"]
)
