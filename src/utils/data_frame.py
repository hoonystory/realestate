import pandas as pd
from src.model.table import Table
from src.utils.log import logger


def create_result_data_frame(result_instance):
    """
    create dataframe for insert database
        - before insert into database, execute preprocessing data type
    :return: df
    """
    # get table information
    from_table = Table(result_instance.get_key())

    # parse each data into appropriate data type
    column_type = from_table.meta_info.get('type')
    for i in range(len(column_type)):
        need_to_parse_type_list = ['integer', 'real']
        current_column_type = column_type[i]

        if need_to_parse_type_list.count(current_column_type) != 0:
            for item in result_instance.get_result_list():
                if current_column_type == 'integer':
                    item[i] = int(item[i].replace(',', ''))
                if current_column_type == 'real':
                    item[i] = float(item[i])

    df = pd.DataFrame(result_instance.get_result_list()
                      , columns=from_table.meta_info.get('columns')) # , dtype=table_info.columns_info
    df.info()
    logger.info(df)

    return df


def verify_insert_data(db_instance, table_name):
    """
    verify inserted data after executing insert query
    :param db_instance:
    :param table_name:
    :return:
    """
    select_sql = 'select * from ' + table_name
    condition_sql = ' limit 5'
    df = get_data_frame_from_database(db_instance, select_sql + condition_sql)
    print(df)


def get_data_frame_from_database(db_instance, query):
    """
    get dataframe from database
    :param db_instance:
    :param query:
    :return:
    """
    db_instance.execute_query(query)
    return pd.DataFrame.from_records(data=db_instance.fetch_all()
                                     , columns=db_instance.get_columns())
