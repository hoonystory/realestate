import datetime
from src.utils.singleton import Singleton


class Calendar(Singleton):
    def __init__(self):
        self.now = datetime.datetime.now()

    def get_today_date(self):
        """
        : 오늘 일자를 리턴
        :return: yyyymmdd
        """
        return self.now.strftime('%Y%m%d')

    def get_today_hour(self):
        """
        : 현재 시간을 리턴
        :return: hh
        """
        return int(self.now.strftime('%H'))

    def get_today_of_week(self):
        """
        : 오늘의 요일을 리턴
        :return: 0~ 6
        """
        return self.now.weekday()

    def get_today_month(self):
        """
        : 이번 달을 리턴
        :return: yyyymm
        """
        return self.now.strftime('%Y%m')