from collections import namedtuple
from datetime import datetime

log_record = namedtuple('log_record', ['msg', 'datetime'])


class Logger:
    LOG_FORMAT = "LOG: %s - %s"

    def __init__(self):
        self._logs = []

    def log_message(self, msg):
        record = log_record(msg=msg, datetime=datetime.utcnow())
        self._logs.append(record)

    def print_messages(self):
        for log in self._logs:
            print(self.LOG_FORMAT % (log.datetime, log.msg))


if __name__ == '__main__':
    logger = Logger()
    logger.log_message('first')
    logger.log_message('second')
    logger.print_messages()
