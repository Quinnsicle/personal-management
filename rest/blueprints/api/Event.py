import csv
import datetime as dt
import io
from flask import (
    Blueprint,
    jsonify,
    request,
)
from flask.views import MethodView
from rest.models import Event as EventModel
from flask_sqlalchemy import *

api = Blueprint("api", __name__, url_prefix="/api")



class Event(MethodView):
    
    @staticmethod
    def output_format(events: list, format: str = "json"):
        if format == "csv":
            csv_out = io.StringIO()
            
            keys = EventModel.__table__.columns.keys()

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
            start_date = dt.datetime.strptime(year_week + "-1", "%Y-W%W-%w").strftime("%Y-%m-%d")
            end_date = dt.datetime.strptime(year_week + "-0", "%Y-W%W-%w").strftime("%Y-%m-%d")
            return self.output_format(EventModel.query.filter(EventModel.start_date_time.between(start_date, end_date)).all(), format)
        if year:
            start_date = "{}-01-01".format(year)
            end_date = "{}-12-31".format(year)
            return self.output_format(EventModel.query.filter(EventModel.start_date_time.between(start_date, end_date)).all(), format)

        return self.output_format(EventModel.query.all(), format)

    def post(self):
        # create a new event
        pass

    def delete(self, event_id):
        # delete a single event
        pass

    def put(self, event_id):
        # update a single event
        pass


event_view = Event.as_view("event_api", EventModel)
api.add_url_rule(
    "/events",
    view_func=event_view,
    methods=[
        "GET",
    ],
)
api.add_url_rule(
    "/",
    view_func=event_view,
    methods=[
        "POST",
    ],
)
api.add_url_rule(
    "/<int:event_id>", view_func=event_view, methods=["GET", "PUT", "DELETE"]
)
