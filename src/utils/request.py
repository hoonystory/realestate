import urllib.request
from bs4 import BeautifulSoup
from src.utils.log import logger


class RequestApi:
    def __init__(self):
        self.url = ''

    def setUrl(self, url):
        self.url = url

    def get_request_result(self):
        if self.url == '':
            logger.error('empty url value!')
            return
        else:
            res = urllib.request.urlopen(self.url)
            result = res.read()
            soup = BeautifulSoup(result, 'lxml-xml')
            items = soup.find_all('item')

            logger.debug(soup)
            logger.debug(items)