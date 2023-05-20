import urllib.request
from bs4 import BeautifulSoup
from src.utils.log import logger


class Request:
    def __init__(self):
        self.url = ''

    def set_url(self, url):
        self.url = url

    def get_request_result(self):
        if self.url == '':
            logger.error('empty url value!')
            return
        else:
            result = urllib.request.urlopen(self.url).read()
            result_items = BeautifulSoup(result, 'lxml-xml').find_all('item')

            for i in result_items:
                logger.debug('dealamount: ' + i.find("거래금액").text)
                logger.debug(i)