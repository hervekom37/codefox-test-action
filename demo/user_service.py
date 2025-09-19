# DEMO FILE: Vulnerable SQL query (injection)
import sqlite3

def find_user_by_username(username):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT);")
    cursor.execute("INSERT INTO users (username, password) VALUES ('alice','pass1')")
    # Bad practice: query concatenation => possible SQL injection
    query = "SELECT id, username FROM users WHERE username = '%s'" % username
    cursor.execute(query)
    return cursor.fetchall()