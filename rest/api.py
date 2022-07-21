import functools
from re import U
import json
from flask import (
    Blueprint,
    g,
    jsonify
)

from rest.db import get_db

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/test", methods=['GET'])
def test_data():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})

@bp.route('/put', methods=['PUT'])
def create_record():
    db = get_db()
    db.execute(
        "INSERT INTO activity (name, start_date_time, end_date_time, category, tags)" " VALUES (work, 2022-07-21T07:00:00.000, 2022-07-21T16:00:00.000, work, ?)",
        (title, body, g.user["id"]),
    )
    db.commit()

    record = json.loads(request.data)
    return jsonify(record)