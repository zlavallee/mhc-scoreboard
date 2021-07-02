import abc
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
        if interval is None:
            self.tick_internal(self._default_interval)
        else:
            self.tick_internal(interval)

    @abc.abstractmethod
    def tick_internal(self, interval):
        pass


class SleepClock(AbstractBaseClock):

    def tick_internal(self, interval):
        time.sleep(interval)
