from src.utils.log import logger
from src.utils.url import URLQueryString
from src.api.request import Request
from src.utils import db
from src.utils import data_frame as from_data


def get_real_txn_apt_trade(LAWD_CD, DEAL_YMD):
    """
    국토교통부 아파트매매 실거래자료
    :param LAWD_CD:
    :param DEAL_YMD:
    :return:
    """

    logger.debug('request for data on real transaction price of apartment trade')

    from_request_info = Request()
    url_object = URLQueryString() \
        .set('LAWD_CD', LAWD_CD) \
        .set('DEAL_YMD', DEAL_YMD)

    # set url info and get result list by requesting api
    from_request_info.set_url('real_txn_apt_trade', url_object)
    result_list = from_request_info.get_request_result_by_xml()

    # convert result list into pandas data frame for saving into database
    data_frame = from_data.create_result_data_frame(result_list)

    # save data from result
    db_instance = db.Sqlite3('data')
    data_frame.to_sql('real_txn_apt_trade', db_instance.conn, if_exists='replace'
              , schema=None, index=False, index_label=None, chunksize=None, dtype=None)
    from_data.verify_inserted_data(db_instance, 'real_txn_apt_trade')

    # show chart from database data

    return

