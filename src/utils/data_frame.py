import pandas as pd
from src.model.table import Table
from src.model import table as from_table
from src.utils.log import logger


def create_result_data_frame(result_instance):
    """
    create result data frame for further use
    :return: df
    """
    # parse each data into appropriate data type
    table_info = Table(result_instance.get_key())

    # for item in result_instance.get_result_list():

    for key, value in table_info.columns_info.items():
        need_to_parse_list = ['integer', 'real']
        if need_to_parse_list.count(value) != 0:
            for item in result_instance.get_result_list():
                index = table_info.columns_array.index(key)
                if value == 'integer':
                    item[index] = int(item[index].replace(',',''))
                if value == 'real':
                    item[index] = float(item[index])

    df = pd.DataFrame(result_instance.get_result_list()
                      , columns=table_info.columns_array) # , dtype=table_info.columns_info
    df.info()
    logger.info(df)

    return df
