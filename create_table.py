from config import cur, conn
'''
Creates the tables needed.

There is already an empty database with all tables created, so no need to run script.
If you wish to make modifications, then you can run script.

Note: The script will drop all pre-existing tables and all data within if executed.
'''

cur.executescript('''
DROP TABLE IF EXISTS doctor;
DROP TABLE IF EXISTS facility;
DROP TABLE IF EXISTS lab;
DROP TABLE IF EXISTS patient;

CREATE TABLE doctor (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    specialization TEXT,
    time TEXT,
    qualification TEXT,
    room_number TEXT
);

CREATE TABLE facility (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE lab (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE,
    cost INTEGER
);

CREATE TABLE patient (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    disease TEXT,
    gender TEXT,
    age INTEGER
);
''')
conn.commit()