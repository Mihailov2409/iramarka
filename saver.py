import sqlite3

def create_db():
    with sqlite3.connect("user_db.db") as connect:
        conn = connect.cursor()
        