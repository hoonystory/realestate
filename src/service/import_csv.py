import pandas as pd
from src.utils import db
from src.utils import file_path as from_variables
from src.model import table as from_table
from src import const


def import_csv(file_nm, db_name, table_name):
    db_instance = db.Sqlite3(db_name)
    file_path = from_variables.get_file_path(from_variables.get_resource_path(), file_nm)

    if from_variables.is_file_exists(file_path):
        df = pd.read_csv(file_path, sep='\t', engine='python', encoding='cp949')
        table_columns = table.get_table_info_from_database(db_name, table_name)
        if table_columns:
            column_array = []
            for key, value in table_columns.items():
                column_array.append(key)
            df.columns = column_array
        df.to_sql(table_name, db_instance.conn, if_exists='replace'
                  , schema=None, index=False, index_label=None, chunksize=None, dtype=None)

    # verify_insert_data(db_instance, table_name)
    db_instance.conn.close()

    # for row in rows:
    #     logger.info(row)


if __name__ == '__main__':
    import_csv('lawd_cd.txt', 'code', 'lawd_cd')
