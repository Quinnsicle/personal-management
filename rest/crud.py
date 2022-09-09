from re import U
import json
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
from rest.models import Event
from rest.database import db_session

bp = Blueprint("crud", __name__, url_prefix="/crud")


@bp.route("/")
def test_data():
    return redirect(url_for("crud.read"))


@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        record = request.form
        db_session.add(Event(record["name"],
                             record["start_date_time"],
                             record["end_date_time"],
                             record["category"],
                             record["tags"],
                             ))
        db_session.commit()
        return redirect(url_for("crud.read"))

    return render_template("create.html")


@bp.route("/read", methods=["GET"])
def read():
    events = Event.query.all()
    return render_template("read.html", events=events)


@bp.route("/update", methods=["POST"])
def update():
    record = json.loads(request.data)

    # update record

    return "updated record-- not yet implemented!!"


@bp.route("/delete", methods=["DELETE"])
def delete():
    request = json.loads(request.data)

    # delete record

    return "deleted record-- not yet implemented!!"
