import pandas as pd
import datetime
import sqlite3
import os

values = {"hangboard": ["DATE", "HANG", "SETS", "REST", "WEIGHT"]}


class Server():
    def __init__(self):
        if not os.path.isfile("data.db"):
            self.create_db()

        self.conn = sqlite3.connect('data.db')

    def post(self, data: dict):
        for k, v in data.items():
            command = f'''INSERT INTO {k} ({",".join(values[k])}) VALUES ({datetime.datetime.now().strftime('%Y%m%d%H%M%S')}, {','.join(v)})'''
            self.conn.execute(command)

        self.conn.commit()

        return 200

    def get(self, request):
        pass

    def delete(self, request):
        pass

    def create_db(self):
        conn = sqlite3.connect('data.db')
        conn.execute('''CREATE TABLE hangboard (
                     ID INTEGER PRIMARY KEY,
                     DATE           TEXT    NOT NULL,
                     HANG           INT     NOT NULL,
                     SETS         INT     NOT NULL,
                     REST           INT     NOT NULL,
                     WEIGHT         REAL    NOT NULL
                     );''')

        conn.execute('''CREATE TABLE pullups (
                             ID INTEGER PRIMARY KEY AUTOINCREMENT,
                             DATE           TEXT    NOT NULL,
                             REPS           INT     NOT NULL,
                             SETS           INT     NOT NULL,
                             PAUSE          INT     NOT NULL,
                             WEIGHT         REAL     NOT NULL
                             );''')

        conn.close()
