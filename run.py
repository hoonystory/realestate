from src.api import apt
from src.utils.log import logger


def main():
    logger.debug('init main')
    apt.get_real_txn_apt_trade('11110', '202001')


if __name__ == '__main__':
    main()
