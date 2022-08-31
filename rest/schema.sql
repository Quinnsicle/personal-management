DROP TABLE IF EXISTS event;
DROP TABLE IF EXISTS user;

CREATE TABLE event (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  start_date_time TEXT NOT NULL,
  end_date_time TEXT NOT NULL,
  category TEXT,
  tags TEXT
  author_id INTEGER NOT NULL
);

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);