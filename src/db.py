import sqlite3
from card import Card

connection = sqlite3.connect("kinkajou.db")
cursor = connection.cursor()

def setup_db(cur=cursor, con=connection):
    try:
        cur.execute("CREATE TABLE vocab(word PRIMARY KEY, answer, written, level)")
        cur.execute("CREATE TABLE levels(level PRIMARY KEY, max, counter)")
    except sqlite3.OperationalError:
        print("Table already exists")
    try:
        cur.execute("INSERT INTO levels VALUES (1, 10, 0), (2, 20, 0), (3, 30, 0), (4, 40, 0), (5, 50, 0)")
        con.commit()
    except sqlite3.IntegrityError:
        print("Levels are set up")

def insert_words(word, answer, written, cur=cursor, con=connection):
    print(f'Inserting into vocab ("{word}","{answer}","{written}",0)')
    cur.execute(f'INSERT INTO vocab VALUES ("{word}","{answer}","{written}",0)')
    con.commit()

def select_cards(level, count):
    cur = connection.cursor()
    cur.row_factory = lambda _, row: Card(*row)
    return cur.execute(f"SELECT * FROM vocab WHERE level = {level} LIMIT {count}").fetchall()

# For debugging run python db.py
if __name__ == '__main__':

    vocab = cursor.execute("SELECT * FROM vocab")
    print("Vocab: ", vocab.fetchall())

    levels = cursor.execute("SELECT * FROM levels")
    print("Levels: ", levels.fetchall())

    cards = select_cards(0, 2)
    print(cards)