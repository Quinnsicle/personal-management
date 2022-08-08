import json
import sqlite3
from rest.dal.db import query_db
from flask import (
    g,
    jsonify,
    request,
)


def create_record(record):
    query_db('INSERT INTO event (name, start_date_time, end_date_time, category, tags)'
             ' VALUES (?, ?, ?, ?, ?)',
             [record['name'], 
              record['start_date_time'], 
              record['end_date_time'], 
              record['category'], 
              record['tags']],
             one=True
             )
    return

def read_all():
    events = query_db(
        'SELECT name, start_date_time, end_date_time, category, tags'
        ' FROM event'
        )
    return events

def read_interval():
    events = query_db(
        'SELECT name, start_date_time, end_date_time, category, tags'
        ' FROM event'
        ' WHERE start_date_time < ? AND end_date_time > ?'
        )
    return events

def read_day():
    events = query_db(
        'SELECT name, start_date_time, end_date_time, category, tags'
        ' FROM event'
        ' WHERE date(start_date_time) < date(?) AND date(end_date_time) > date(?)',
        (),
        one=True
        )
    return events

def read_week():
    events = query_db(
        'SELECT name, start_date_time, end_date_time, category, tags'
        ' FROM event'
        ' WHERE start_date_time < ? AND end_date_time > ?'
        )
    return events

def read_month():
    events = query_db(
        'SELECT name, start_date_time, end_date_time, category, tags'
        ' FROM event'
        ' WHERE start_date_time < ? AND end_date_time > ?'
        )
    return events

def update_record(record):
    query_db(
        'UPDATE table'
        ' SET name = ?,'
        ' WHERE id = ? ',
        (record['name'],
         record['id'])
    )
    return

def delete_record(record):
    query_db(
        'DELETE from event'
        ' WHERE start_date_time = ? AND end_date_time = ?',
        (record['start_date_time'],
         record['end_date_time'])
    )
    return
