import sqlite3

connection = sqlite3.connect("kinkajou.db")
cursor = connection.cursor()


def setup_db(cur=cursor, con=connection):
    try:
        cur.execute("CREATE TABLE vocab(value PRIMARY KEY, answer, written, level)")
        cur.execute("CREATE TABLE levels(level PRIMARY KEY, max, counter)")
    except sqlite3.OperationalError:
        print("Table already exists")
    try:
        cur.execute("INSERT INTO levels VALUES (1, 10, 0), (2, 20, 0), (3, 30, 0), (4, 40, 0), (5, 50, 0)")
        con.commit()
    except sqlite3.IntegrityError:
        print("Levels are set up")


def insert_values(value, answer, written, cur=cursor, con=connection):
    cur.execute(f'INSERT INTO vocab VALUES ("{value}","{answer}","{written}",0)')
    con.commit()


res = cursor.execute("SELECT * FROM vocab")

print(res.fetchall())
