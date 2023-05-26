from src.api import apt
from src.utils.log import logger


def main():
    logger.debug('init main')
    apt.get_real_txn_apt_trade('11110', '202001')

    # todo: set class configuration
    #   - main class: contains db, calendar instance
    #   - sub class; use db, calendar,.. and some other instances by inheriting main class


if __name__ == '__main__':
    main()
