import sqlite3


class Database:
    def __init__(self):
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect('todo.db')
        return self.conn

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.commit()
        self.conn.close()
