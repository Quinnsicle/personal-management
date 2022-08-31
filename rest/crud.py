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
from rest.dal.event import *

bp = Blueprint("crud", __name__, url_prefix="/crud")


@bp.route("/")
def test_data():
    return redirect(url_for("crud.read"))


@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        create_record(request.form)
        return redirect(url_for("crud.read"))

    return render_template("create.html")


@bp.route("/read", methods=["GET"])
def read():
    events = read_all_records()

    return render_template("read.html", events=events)


@bp.route("/update", methods=["POST"])
def update():
    record = json.loads(request.data)

    update_record(record)

    return "updated record"


@bp.route("/delete", methods=["DELETE"])
def delete():
    request = json.loads(request.data)

    delete_record(request)

    return "deleted record"
