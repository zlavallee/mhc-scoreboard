import abc
import logging


class ShiftRegister(abc.ABC):

    @abc.abstractmethod
    def send_byte(self, data) -> None:
        pass

    @abc.abstractmethod
    def store_data(self) -> None:
        pass


class StubShiftRegister(ShiftRegister):

    def __init__(self, enable_logging=True):
        self._enable_logging = enable_logging

    def send_byte(self, data) -> None:
        if self._enable_logging:
            logging.debug('Sending byte: {}'.format(data))
        pass

    def store_data(self) -> None:
        if self._enable_logging:
            logging.debug('Storing data.')
        pass
