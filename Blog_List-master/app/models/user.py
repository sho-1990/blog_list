# -*- coding:utf-8 -*-

from sql import sqliteconn

class User:

    def __init__(self, user={}):
        USER_NAME = user['user']
        PASSWORD = user['pass']

    def __init__(self):

    def selectUser(self, user={}):

        con = sqliteconn.userDb()
        con.execute("""
            select * from users where username = %s and password = %s

           """) % USER_NAME, PASSWORD

        con.commit()
        con.close()
