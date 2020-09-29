# -*- coding: utf-8 -*-

import sqlite3


class DataBase:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(self.name + ".db")
        self.cursor = self.conn.cursor()

    def execute(self, query, args=()):
        self.cursor.execute(query, args)
        res = self.cursor.fetchall()
        self.conn.commit()
        return (res[0] if res else None) if False else res

    def __del__(self):
        self.conn.close()
