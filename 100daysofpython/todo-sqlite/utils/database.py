import sqlite3
from sqlite3 import Error
from utils.database_connection import Database


def create_table():
    with Database() as db:
        query = """CREATE TABLE IF NOT EXISTS TODO (
            ID INTEGER PRIMARY KEY,
            TITLE CHAR(100) NOT NULL,
            COMPLETED INTEGER DEFAULT 0 NOT NULL
        )
        """
        try:
            db.execute(query)
            # print('Database created successfully.')
        except Error as e:
            print(e)


def insert_into_db(params):
    with Database() as db:
        query = """
        INSERT INTO TODO (TITLE) VALUES (?)
        """
        try:
            db.execute(query, params)
            print('Inserted into db')
        except Error as e:
            print(e)


def update_todo(params):
    with Database() as db:
        query = """
        UPDATE TODO set COMPLETED = 1 where ID = (?)
        """
        try:
            db.execute(query, params)
        except Error as e:
            print(e)


def delete_todo(params):
    with Database() as db:
        query = """DELETE FROM TODO WHERE ID = (?)"""
        try:
            db.execute(query, params)
        except Error as e:
            print(e)


def get_queryset():
    with Database() as db:
        query = """
        SELECT * FROM TODO
        """
        return [
            {"id": row[0], "todo":row[1], "completed":row[2]} for row in db.execute(query)
        ]
