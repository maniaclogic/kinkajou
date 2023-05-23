import sqlite3


connection = sqlite3.connect("kinkajou.db")
cursor = connection.cursor()


def setup_db(cur):
    cur.execute("CREATE TABLE vocab(value PRIMARY KEY, answer, written, level INTEGER DEFAULT 0)")
    cur.execute("CREATE TABLE levels(level PRIMARY KEY, max, counter)")


def setup_levels(cur, con):
    cur.execute("INSERT INTO levels VALUES (1, 10, 0), (2, 20, 0), (3, 30, 0), (4, 40, 0), (5, 50, 0)")
    con.commit()


try:
    setup_db(cursor)
except sqlite3.OperationalError:
    print("Table already exists")

try:
    setup_levels(cursor, connection)
except sqlite3.IntegrityError:
    print("Levels are set up")

res = cursor.execute("SELECT * FROM levels")

print(res.fetchall())
