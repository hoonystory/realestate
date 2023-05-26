from src.utils import db
from src.model import table
from src.utils.log import logger


def get_conn_and_create_table_if_empty(db_name, table_name):
    sql = 'select count(*) from sqlite_master where name = "' + table_name + '"'

    db_instance = db.Sqlite3(db_name)
    db_instance.cursor.execute(sql)

    result = db_instance.cursor.fetchone()
    if result[0] != 1:
        table_info = table.get_table_info_from_database(db_name, table_name)
        if table_info:
            column_array = []
            for key, value in table_info.items():
                column_array.append(key + ' ' + value)
            sql = 'create table if not exists ' + table_name
            sql += ' (' + ', '.join(column_array) + ')'

            logger.info(sql)
            db_instance.cursor.execute(sql)
            db_instance.conn.commit()

    return db_instance
