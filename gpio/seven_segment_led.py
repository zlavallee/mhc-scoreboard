import itertools
import logging

from config import config
from gpio.gpio_adapter import SN74HC595NOutput, create_output_from_config


def create_seven_segment_led(output_config):
    return SevenSegmentLed(
        output_device=create_output_from_config(output_config),
        digit_dictionary=config.get_dictionary()
    )


class SevenSegmentLed:

    def __init__(self, output_device: SN74HC595NOutput, digit_dictionary):
        self.digit_dictionary = digit_dictionary
        self.output_device = output_device

    def clear(self, digits=1, clear_value="_"):
        for _ in itertools.repeat(digits):
            self.output_device.send_byte(self.get_hex_value(clear_value))

        self.output_device.store_data()

    def set_values(self, values):
        logging.debug('Setting values: {}'.format(values))
        hex_data = self.convert_to_hex(values)
        logging.debug('Hex: {}'.format(hex_data))
        for data in hex_data:
            logging.debug('Sending byte: {}'.format(data))
            self.output_device.send_byte(data)

        logging.debug('Storing date...')
        self.output_device.store_data()

    def convert_to_hex(self, values):
        hex_data = []

        for string_value in values:
            hex_data.insert(0, self.get_hex_value(string_value))

        return hex_data

    def get_hex_value(self, value):
        hex_value = self.digit_dictionary[value]

        if hex_value is None:
            raise Exception(
                'Invalid string value send to display. '
                'Dictionary does not contain definition character value: {}'.format(value))

        return hex_value
