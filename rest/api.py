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
from rest.dal.db import get_db

bp = Blueprint("api", __name__, url_prefix="/api")


def create_record(record):
    db = get_db()
    db.execute(
        "INSERT INTO event (name, start_date_time, end_date_time, category, tags)" 
        " VALUES (?, ?, ?, ?, ?)",
        (record['name'], 
         record['start_date_time'], 
         record['end_date_time'], 
         record['category'], 
         record['tags'])
    )
    db.commit()
    return

def read_all_records():
    db = get_db()
    events = (
        db.execute(
            "SELECT name, start_date_time, end_date_time, category, tags"
            " FROM event"
        )
    ).fetchall()
    return events

def update_record(record):
    db = get_db()
    db.execute(
        "UPDATE table"
        "SET name = ?,"
        "WHERE id = ? ",
        (record['name'],
         record['id'])
    )
    db.commit()
    return

def delete_record(record):
    db = get_db()
    db.execute(
        "DELETE from event"
        "WHERE start_date_time = ? AND end_date_time = ?",
        (record['start_date_time'],
         record['end_date_time'])
    )
    db.commit()
    return
