import pandas as pd
from src.model.table import Table
from src.utils.log import logger


def create_result_data_frame(result_instance):
    """
    create result data frame for further use
    :return: df
    """
    # parse each data into appropriate data type
    from_table = Table(result_instance.get_key())

    # for item in result_instance.get_result_list():
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
