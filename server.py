import sqlite3
import hashlib

connection = sqlite3.connect('data.db', check_same_thread=False)
cursor = connection.cursor()


def auto_increment_null():
    cursor.execute('UPDATE sqlite_sequence SET seq = 1 WHERE name = "recipes"')


def log_in(username, password):
    cursor.execute("SELECT * FROM users WHERE username = ?", [username])
    result = cursor.fetchone()
    if result is not None:
        if hashlib.sha256(password.encode()).hexdigest() == result[2]:
            return 'Successful'
        else:
            return 'Invalid password'
    else:
        return "The user does not exist"


def verification(username, email):
    pass


# Регистрация в аккаунт
def sign_up(username, password, email):
    cursor.execute("SELECT * FROM users WHERE username = ?", [username])
    if cursor.fetchone() is None:
        cursor.execute('SELECT * FROM users WHERE email = ?', [email])
        if cursor.fetchone() is None:
            hash_pass = hashlib.sha256(password.encode())
            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                           [username, email, str(hash_pass.hexdigest())])
            connection.commit()
            return 'Successful'
        else:
            return
    else:
        return 'Username is occupied'


def get_all_articles():
    cursor.execute('SELECT * FROM recipes')
    return cursor.fetchall()


def get_recipe(id):
    cursor.execute('SELECT * FROM recipes WHERE id = ?', [id])
    return cursor.fetchone()


connection.commit()
