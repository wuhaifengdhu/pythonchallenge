import time


class DateHelper(object):

    @staticmethod
    def get_current_timestamp():
        return str(int(time.time()))
