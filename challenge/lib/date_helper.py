import time
from datetime import date


class DateHelper(object):

    @staticmethod
    def get_current_timestamp():
        return str(int(time.time()))

    @staticmethod
    def get_current_date():
        return str(date.today())
