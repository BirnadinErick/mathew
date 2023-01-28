import sqlite3
from datastore import DataStore


class SqliteStore(DataStore):
    def __init__(self, filename):
        # bootstrap the queries
        self._create_query = "CREATE TABLE tbl(key,data)"
        self._insert_query = "INSERT INTO tbl(key,data) VALUES(?,?)"
        self._select_query = "SELECT data FROM tbl WHERE key=?"

        # establish a connection
        self.conn = sqlite3.connect(filename)

    def __enter__(self):
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        self.conn.close()

    def get_data(self):
        curr = self.conn.cursor()
        res = curr.execute(f"SELECT * FROM tbl")
        return res.fetchall()

    def bootstrap(self):

        # create and populate init data
        curr = self.conn.cursor()
        _ = curr.execute(self._create_query)
        self.conn.commit()
        fake_data = [
            ("info", "<h3>Information Hidden in Metafile</h3>",),
            ("uname", "<p>Username: BirnE</p>",),
            ("link", "<a href=\"https://www.google.com\">Google</a>",),
        ]
        _ = curr.executemany(self._insert_query, fake_data)
        self.conn.commit()
