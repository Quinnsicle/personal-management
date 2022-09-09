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

            keys = events[0].keys()

            dict_writer = csv.DictWriter(csv_out, keys)
            dict_writer.writeheader()
            dict_writer.writerows(events)

            return csv_out.getvalue()

        if format == "json":
            return json.dumps(events)

        return "sorry, this api doesn't support " + format

    def get(self):
        year = request.args.get("year")
        week = request.args.get("week")
        format = request.args.get("format")
        if format is None:
            format = "json"
        if year and week:
            return self.output_format(read_all_records_within_week(year, week), format)
        if year:
            return self.output_format(read_all_records_within_year(year), format)

        events = read_all_records()
        return self.output_format(read_all_records(), format)

    def post(self):
        # create a new event
        pass

    def delete(self, event_id):
        # delete a single event
        pass

    def put(self, event_id):
        # update a single event
        pass



class Events2(MethodView):
    @staticmethod
    def output_format(events: list, format: str = "json"):
        if format == "csv":
            csv_out = io.StringIO()
            
            header_columns = events[0].headers()

            writer = csv.writer(csv_out, header_columns)
            writer.writerow(header_columns)
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
            return self.output_format(Event.query.filter(Event.extract('year', Event.start_date_time) == year).all(), format)
        if year:
            return self.output_format(Event.query.filter(Event.extract('year', Event.start_date_time) == year).all(), format)

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


event_view = Events2.as_view("events_api2")
bp.add_url_rule(
    "/events2",
    view_func=event_view,
    methods=[
        "GET",
    ],
)

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
