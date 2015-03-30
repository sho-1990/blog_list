import mysql.connector

config = {
    'user' : 'root',
    'password' : 'root',
    'host' : 'localhost'
}

class Connector:

    def __init__(self):
        self.cnx = mysql.connector.connect(**config)
        self.cur = self.cnx.cursor(buffered=True)

    def get_conn(self):
        return self.cur

    def close(self):
        self.cur.close()
        self.cnx.close()

# test
connector = Connector()
conn = connector.get_conn()
conn.execute("select * from blog_list.urls")
for i in conn:
    print(i)
connector.close()