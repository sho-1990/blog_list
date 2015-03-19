# -*- coding: utf-8 -*-

import sqlite3
from connection import CreateConn

DROP_URLS = """DROP TABLE IF EXISTS urls;"""

CREATE_URLS = """CREATE TABLE urls (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        url VARCHAR(255),
                                        site_name VARCHAR(255),
                                        regdate DATETIME
                                        );"""

conn = CreateConn().get_conn('urls.db')

cur = conn.cursor()

cur.execute(DROP_URLS)
cur.execute(CREATE_URLS)

conn.commit()

