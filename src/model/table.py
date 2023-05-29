class Table:
    def __init__(self, tbl):
        self.meta_info = None
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
                self.meta_info = v
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


def get_specific_table_info(tbl, key):
    table_info = table.get(tbl)
    if table_info:
        return table_info.get(key, [])
    return []


def get_data_result_column(tbl):
    return get_specific_table_info(tbl, 'columns')


def get_data_result_description(tbl):
    return get_specific_table_info(tbl, 'description')


def get_table_columns_type(tbl):
    return get_specific_table_info(tbl, 'type')


def get_table_request_params(tbl):
    return get_specific_table_info(tbl, 'request')

# DATABASE_CODE = 'code'
# DATABASE_DATA = 'data'


table = {
    'lawd_cd': {
        'columns': [
            'lawd_cd', 'dong_nm', 'exyn'
        ],
        'type': [
            'integer', 'text', 'text'
        ],
        'description': [
            '법정동코드', '법정동명', '폐지여부'
        ],
        'database': 'code'
    },
    'real_txn_apt_trade': {
        'columns': [
            'deal_amount', 'build_year', 'deal_year'
            , 'dong_nm', 'apartment', 'deal_month'
            , 'deal_day', 'exclusive_area', 'jibun'
            , 'lawd_cd', 'floor'
        ],
        'type': [
            'integer', 'integer', 'integer'
            , 'text', 'text', 'integer'
            , 'integer', 'text', 'text'
            , 'integer', 'integer'
        ],
        'description': [
            '거래금액', '건축년도', '년'
            , '법정동', '아파트', '월'
            , '일', '전용면적', '지번'
            , '지역코드', '층'
        ],
        'request': [
            'lawd_cd', 'deal_ymd'
        ],
        'database': 'data'
    }
}
