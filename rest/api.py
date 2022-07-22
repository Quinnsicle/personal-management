import functools
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

from rest.db import get_db

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/test", methods=['GET'])
def test_data():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})

@bp.route('/create', methods=['GET', 'POST'])
def create_record():
    if request.method == "POST":
        db = get_db()
        db.execute(
            "INSERT INTO activity (name, start_date_time, end_date_time, category, tags)" 
            " VALUES (?, ?, ?, ?, ?)",
            (request.form['name'], request.form['start_date_time'], request.form['end_date_time'], request.form['category'], request.form['tags'])
        )
        db.commit()
        return redirect(url_for("api.query_records"))

    return render_template("create.html")

@bp.route('/read', methods=['GET'])
def query_records():

    db = get_db()
    events = (
        db.execute(
            "SELECT name, start_date_time, end_date_time, category, tags FROM activity"
        )
    ).fetchall()

    return render_template("read.html", events=events)

@bp.route('/update', methods=['POST'])
def update_record():
    record = json.loads(request.data)

    db = get_db()
    db.execute(
        "UPDATE table"
        "SET name = ?,"
        "WHERE id = ? ",
        (record['name'], record['id'])
    )
    db.commit()

    return "updated record"
    
@bp.route('/delete', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)

    db = get_db()
    db.execute(
        "DELETE from activity"
        "WHERE start_date_time = ? AND end_date_time = ?",
        (record['start_date_time'], record['end_date_time'])
    )
    db.commit()

    return "deleted record"
