from src.utils.log import logger
from src.utils.url import URLQueryString
from src.api.common import Request


def get_real_txn_apt_trade(LAWD_CD, DEAL_YMD):
    """
    국토교통부 아파트매매 실거래자료
    :param LAWD_CD:
    :param DEAL_YMD:
    :return:
    """

    logger.debug('request for data on real transaction price of apartment trade')

    request_api = Request()
    url_object = URLQueryString() \
        .set('LAWD_CD', LAWD_CD) \
        .set('DEAL_YMD', DEAL_YMD)

    request_api.set_url('real_txn_apt_trade', url_object)
    request_api.get_request_result()

    # todo: save data from result
    # todo: show chart from database data

    return
