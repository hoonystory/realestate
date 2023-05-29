from src.api import apt
from src.utils.log import logger
from src.model.param import Parameter


def main():
    logger.debug('init main')

    # todo.. 1) set class configuration
    #   - main class: contains db, calendar instance
    #   - sub class; use db, calendar,.. and some other instances by inheriting main class

    # todo.. 2) set time when will save data
    #   - period till next time

    # todo.. 3) set regional code to be saved in database
    #   - only for Seoul region

    apt_txn_trade_param \
        = Parameter('real_txn_apt_trade', '11110', '202001')

    apt.get_real_txn_apt_trade(apt_txn_trade_param)


if __name__ == '__main__':
    main()
