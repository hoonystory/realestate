import sqlite3
from src import const
from src.utils import file_path as from_variables


class Sqlite3:
    db_path = ''
    conn = None
    cursor = None

    def __init__(self, *args):
        # set database file path with first argument
        if len(args) != 0:
            self.db_path = from_variables.get_file_path(from_variables.get_database_path(), args[0] + '.db')

        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
