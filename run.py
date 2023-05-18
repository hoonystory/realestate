from src import const
from src.api import apt
from src.utils.log import logger


def main():
    logger.debug('init main')
    apt.getRTMSDataSvcAptTrade('11110', '202001', const.api_access_key)


if __name__ == '__main__':
    main()
