import functools
from re import U
import json
from werkzeug.exceptions import abort
from flask import (
    Blueprint,
    g,
    jsonify,
    request,
)

from rest.db import get_db

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/test", methods=['GET'])
def test_data():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})

@bp.route('/get', methods=['GET'])
def query_records():

    db = get_db()
    event = (
        db.execute(
            "SELECT name, start_date_time, end_date_time, category, tags FROM activity"
        )
    ).fetchone()

    
    if event is None:
        abort(404, f"event doesn't exist.")

    return jsonify({'name': event['name'],
                    'start_date_time': event['start_date_time'],
                    'end_date_time': event['end_date_time'],
                    'category': event['category'],
                    'tags': event['tags']})

@bp.route('/put', methods=['GET', 'PUT'])
def create_record():
    db = get_db()
    db.execute(
        "INSERT INTO activity (name, start_date_time, end_date_time, category, tags)" 
        " VALUES ('work', datetime('2022-07-21 07:00'), datetime('2022-07-21 16:00'), 'work', 'aoeu')",
        ()
    )
    db.commit()

    return "created record"

@bp.route('/post', methods=['POST'])
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
def delte_record():
    record = json.loads(request.data)

    db = get_db()
    db.execute(
        "DELETE from activity"
        "WHERE start_date_time = ? AND end_date_time = ?",
        (record['start_date_time'], record['end_date_time'])
    )
    db.commit()

    return "deleted record"
