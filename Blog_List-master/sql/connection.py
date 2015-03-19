# -*- coding: utf-8 -*-

import sqlite3

class CreateConn:

    def __init__(self):
        pass

    def get_conn(self, db_name = ""):

        self._db_name = db_name

        if(self._db_name != ""):
            self.conn = sqlite3.connect(self._db_name)
            return self.conn
        else:
            print("DB名を指定して下さい。")

    def commit():
        self.conn.commit()