def get_database_table_info(db, tbl):
    """
    get database table information
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


table = {
    'code': {
        'lawd_cd': {
            'lawd_cd': 'integer'
            , 'dong_nm': 'text'
            , 'exyn': 'text'
        }
    }
}