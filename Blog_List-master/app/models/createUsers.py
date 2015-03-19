# -*- coding:utf-8 -*-

from sql import sqliteconn as sqcon

con = sqcon.userDb()

sql = """
            create table users (
                user vachar(40),
                password varchar(40));
        """

con.execute(sql)
con.commit()