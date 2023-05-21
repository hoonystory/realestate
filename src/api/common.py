import urllib.request
from bs4 import BeautifulSoup
from src import const
from src.utils.url import URLQueryString
from src.utils.log import logger


class Request:
    def __init__(self):
        self.url = ''
        self.key = ''

    def set_url(self, key, from_url_instance):
        self.key = key

        from_url_instance.set('serviceKey', const.get_request_info('access_key'))
        self.url = const.get_request_info('request_url') \
                   + const.get_request_info(self.key) + from_url_instance.get_query_string()

    def get_request_result(self):
        if self.url == '':
            logger.error('empty url value!')
            return
        else:
            result = urllib.request.urlopen(self.url).read()
            result_items = BeautifulSoup(result, 'lxml-xml').find_all('item')
            result_array = []

            for i in result_items:
                result_item = []
                for value in const.get_data_result_column(self.key).items():
                    result_item.append(i.find(value).text.strip())
                result_array.append(result_item)
                # logger.debug(i)

            logger.debug(result_items)
            logger.debug(result_array)