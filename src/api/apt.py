from src.const import const
from src.utils.log import logger
from src.utils.url import URLQueryString
from src.api.common import Request


def get_real_txn_apt_trade(LAWD_CD, DEAL_YMD, serviceKey):
    """
    국토교통부 아파트매매 실거래자료
    :param LAWD_CD:
    :param DEAL_YMD:
    :param serviceKey:
    :return:
    """

    logger.debug('request for data on real transaction price of apartment trade')

    request_api = Request()
    from_array = URLQueryString() \
        .set('LAWD_CD', LAWD_CD) \
        .set('DEAL_YMD', DEAL_YMD) \
        .set('serviceKey', serviceKey)

    result_url = const.api_request_url + const.svc_apt_trade_url + from_array.get_query_string()

    logger.debug('requestUrl: '
                 + const.svc_apt_trade_url + from_array.get_except_service_key())

    request_api.set_url(result_url)
    request_api.get_request_result()

    return
