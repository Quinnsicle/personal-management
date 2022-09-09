import json
import sqlite3
from rest.db import get_db
from flask import (
    g,
    jsonify,
    request,
)
import datetime


def create_record(record):
    db = get_db()
    db.execute(
        "INSERT INTO event (name, start_date_time, end_date_time, category, tags)"
        " VALUES (?, ?, ?, ?, ?)",
        (
            record["name"],
            record["start_date_time"],
            record["end_date_time"],
            record["category"],
            record["tags"],
        ),
    )
    db.commit()
    return


def read_all_records():
    db = get_db()
    rows = (
        db.execute(
            "SELECT name, start_date_time, end_date_time, category, tags" " FROM event"
        )
    ).fetchall()
    events = [dict(row) for row in rows]
    return events


def read_all_records_within_year(year):
    start_date = "{}-01-01".format(year)
    end_date = "{}-12-31".format(year)
    db = get_db()
    rows = (
        db.execute(
            "SELECT name, start_date_time, end_date_time, category, tags"
            " FROM event WHERE date(start_date_time) BETWEEN ? AND ?",
            (start_date, end_date),
        )
    ).fetchall()
    events = [dict(row) for row in rows]
    return events


def read_all_records_within_week(year, week):
    year_week = "{}-W{}".format(year, week)
    start_date = datetime.datetime.strptime(year_week + "-1", "%Y-W%W-%w").strftime(
        "%Y-%m-%d"
    )
    end_date = datetime.datetime.strptime(year_week + "-0", "%Y-W%W-%w").strftime(
        "%Y-%m-%d"
    )
    db = get_db()
    rows = (
        db.execute(
            "SELECT name, start_date_time, end_date_time, category, tags"
            " FROM event WHERE date(start_date_time) BETWEEN ? AND ?",
            (
                start_date,
                end_date,
            ),
        )
    ).fetchall()
    events = [dict(row) for row in rows]
    return events


def update_record(record):
    db = get_db()
    db.execute(
        "UPDATE table" "SET name = ?," "WHERE id = ? ", (record["name"], record["id"])
    )
    db.commit()
    return


def delete_record(record):
    db = get_db()
    db.execute(
        "DELETE from event" "WHERE start_date_time = ? AND end_date_time = ?",
        (record["start_date_time"], record["end_date_time"]),
    )
    db.commit()
    return
