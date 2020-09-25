# -*- coding: utf-8 -*-

import sqlite3


class DataBase:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(self.name + ".db")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()
