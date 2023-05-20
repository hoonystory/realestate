from src.api import apt
from src.const import const
from src.utils.log import logger


def main():
    logger.debug('init main')
    apt.get_real_txn_apt_trade('11110', '202001', const.api_access_key)


if __name__ == '__main__':
    main()
