from src.utils import db


def get_lawd_cd_list():
    db_instance = db.Sqlite3('code')