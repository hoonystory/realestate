from src.utils.log import logger
from src.utils.url import URLQueryString
from src.api.request import Request
from src.utils import db
from src.utils import data_frame as from_data


def get_real_txn_apt_trade(params):
    """
    국토교통부 아파트매매 실거래자료
    :param params:
    :return:
    """

    logger.debug('request for data on real transaction price of apartment trade')

    db_table_nm = params.table_nm
    db_instance = db.Sqlite3('data')

    # before request api, check database if it already has selected data
    verify_query = 'select exists ( ' \
                   'select 1 ' \
                   'from ' + db_table_nm + \
                   'where lawd_cd like "11110%" and deal_ymd like "" ' \
                   'limit 5 )'

    # set url info and get result list by requesting api
    from_request_info = Request()
    url_object = URLQueryString()
    for key, value in params.dict:
        url_object.set(key, value)

    from_request_info.set_url(db_table_nm, url_object)
    result_list = from_request_info.get_request_result_by_xml()

    # convert result list into pandas data frame for saving into database
    data_frame = from_data.create_result_data_frame(result_list)

    # save data from result
    data_frame.to_sql(db_table_nm, db_instance.conn, if_exists='replace'
              , schema=None, index=False, index_label=None, chunksize=None, dtype=None)
    from_data.verify_insert_data(db_instance, db_table_nm)

    # show chart from database data

    return

