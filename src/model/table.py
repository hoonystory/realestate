class Table:
    def __init__(self, tbl):
        self.columns_info = None
        self.columns_array = []
        self.get_table_columns_info(table, tbl)

    def get_table_columns_info(self, d, tbl):
        """
        get table column information by recursive iteration
        :param d:
        :param tbl:
        :return: dict
        """
        for k, v in d.items():
            if k == tbl:
                # set table columns information
                self.columns_info = v
                for key, value in self.columns_info.items():
                    self.columns_array.append(key)
            if isinstance(v, dict):
                self.get_table_columns_info(v, tbl)


def get_table_info_from_database(db, tbl):
    """
    get table information from specific database
    :param db:
    :param tbl:
    :return:
    """
    is_empty = True
    selected_database = table.get(db, is_empty)
    if is_empty != selected_database:
        selected_table = selected_database.get(tbl, is_empty)
        if is_empty != selected_table:
            return selected_table
        else:
            return False


DATABASE_CODE = 'code'
DATABASE_DATA = 'data'

table = {
    DATABASE_CODE: {
        'lawd_cd': {
            'lawd_cd': 'integer'
            , 'dong_nm': 'text'
            , 'exyn': 'text'
        }
    },
    DATABASE_DATA: {
        'real_txn_apt_trade': {
            'dealAmount': 'integer'
            , 'buildYear': 'integer'
            , 'dealYear': 'integer'
            , 'dong': 'text'
            , 'apartment': 'text'
            , 'dealMonth': 'integer'
            , 'dealDay': 'integer'
            , 'exclusiveArea': 'text'
            , 'jibun': 'text'
            , 'regionCode': 'integer'
            , 'floor': 'integer'
        }
    }
}
