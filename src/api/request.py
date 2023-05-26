import urllib.request
from bs4 import BeautifulSoup
from src import const
from src.model import table
from src.model.result import List
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

    def get_request_result_by_xml(self):
        if self.url == '':
            logger.error('empty url value!')
            return
        else:
            result = urllib.request.urlopen(self.url).read()
            result_items = BeautifulSoup(result, 'lxml-xml').find_all('item')
            result_list = List().set_key(self.key)

            for i in result_items:
                result_item = []
                # parse xml into python list data
                for description in table.get_data_result_description(self.key):
                    result_item.append(i.find(description).text.strip())

                result_list.get_result_list().append(result_item)

            return result_list
