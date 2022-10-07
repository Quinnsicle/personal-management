from typing import Union
import jsonschema
import sqlalchemy as sa
from datetime import datetime
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from jsonschema import validate

db = SQLAlchemy()


@dataclass
class Event(db.Model):
    __tablename__ = 'event'
    id: int = sa.Column(sa.Integer, primary_key=True)
    name: str = sa.Column(sa.String(40), nullable=False)
    start_date_time: datetime = sa.Column(sa.DateTime, nullable=False)
    end_date_time: datetime = sa.Column(sa.DateTime, nullable=False)
    category: str = sa.Column(sa.String(40), nullable=True)
    tags: str = sa.Column(sa.String(40), nullable=True)
    author_id: str = sa.Column(
        sa.String(20), sa.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, start_date_time, end_date_time, category=None, tags=None, author_id='test'):
        self.name = name
        self.start_date_time = datetime.fromisoformat(start_date_time)
        self.end_date_time = datetime.fromisoformat(end_date_time)
        self.category = category
        self.tags = tags
        self.author_id = author_id

    def __repr__(self):
        return f'''
<Event id={self.id!r},
 name={self.name!r},
 start_date_time={self.start_date_time!r},
 end_date_time={self.end_date_time!r},
 category={self.category!r},
 tags={self.tags!r},
 author_id={self.author_id!r} >'''

    def validate(json):
        # Describe what kind of json you expect.
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "name": {"type": "string"},
                "author_id": {"type": "string"},
                "start_date_time": {"type": "string"},
                "end_date_time": {"type": "string"},
                "category": {"type": "string"},
                "tags": {"type": "string"},
            }
        }

        try:
            validate(instance=json, schema=schema)
        except jsonschema.exceptions.ValidationError:
            return False

        return True

    @classmethod
    def from_json(cls, data: Union[list, dict]):
        event = cls(data['name'], data['start_date_time'], data['end_date_time'],
                    data['category'], data['tags'], data['author_id'])
        return event


class User(db.Model):
    __tablename__ = 'user'
    id: int = sa.Column(sa.Integer, primary_key=True)
    username: str = sa.Column(sa.String(20), unique=True, nullable=False)
    password: str = sa.Column(sa.String(30), unique=True, nullable=False)

    # relationships
    events = sa.orm.relationship('Event', backref='user', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'''
<User id={self.id!r},
 username={self.username!r},
 password={self.password!r} >'''
