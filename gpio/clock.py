import abc
import logging
import time


def create_sleep_clock(interval):
    return SleepClock(interval)


class Clock(abc.ABC):
    def __init__(self, default_interval):
        self._default_interval = default_interval

    @abc.abstractmethod
    def tick(self, interval):
        pass


class AbstractBaseClock(abc.ABC):
    def __init__(self, default_interval):
        self._default_interval = default_interval

    def tick(self, interval=None):
        temp_interval = interval

        if temp_interval is None:
            temp_interval = self._default_interval

        logging.info('Tick for {} seconds', temp_interval)
        self.tick_internal(temp_interval)

    @abc.abstractmethod
    def tick_internal(self, interval):
        pass


class SleepClock(AbstractBaseClock):

    def tick_internal(self, interval):
        logging.info('Sleeping for {} seconds'.format(interval))
        time.sleep(interval)
