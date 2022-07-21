DROP TABLE IF EXISTS activity;

CREATE TABLE activity (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  start_date_time TEXT NOT NULL,
  end_date_time TEXT NOT NULL,
  category TEXT,
  tags TEXT
);