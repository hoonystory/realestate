from src import const
from src.utils.log import logger
from src.utils.url import URLQueryString
from src.utils.request import RequestApi


def getRTMSDataSvcAptTrade(LAWD_CD, DEAL_YMD, serviceKey):

    logger.debug('request for data on real transaction price of apartment trade')

    request_api = RequestApi()
    from_array = URLQueryString() \
        .set('LAWD_CD', LAWD_CD) \
        .set('DEAL_YMD', DEAL_YMD) \
        .set('serviceKey', serviceKey)

    result_url = const.api_request_url + const.svc_apt_trade_url + from_array.get_query_string()

    logger.debug('requestUrl: '
                 + const.svc_apt_trade_url + from_array.get_except_service_key())

    request_api.setUrl(result_url)
    request_api.get_request_result()

    return
