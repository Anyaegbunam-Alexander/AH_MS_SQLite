import sqlite3

#connects to the SQLite database
conn = sqlite3.connect('AH_MS.sqlite')
cur = conn.cursor()
