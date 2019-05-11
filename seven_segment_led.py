import itertools

from gpio_adapter import SN74HC595NOutput

cathode_digit_dictionary = {
    "_": 0x00,
    "0": 0x3F,
    "1": 0x06,
    "2": 0x5B,
    "3": 0x4F,
    "4": 0x66,
    "5": 0x6D,
    "6": 0x7D,
    "7": 0x07,
    "8": 0x7F,
    "9": 0x67,
}

anode_digit_dictionary = {
    "_": 0xFF,
    "0": 0xC0,
    "1": 0xF9,
    "2": 0xA4,
    "3": 0xB0,
    "4": 0x99,
    "5": 0x92,
    "6": 0x82,
    "7": 0xF8,
    "8": 0x80,
    "9": 0x98,
}


class SevenSegmentLed:

    def __init__(self, output_device: SN74HC595NOutput, digit_dictionary=None):
        self.digit_dictionary = digit_dictionary
        self.output_device = output_device

        if digit_dictionary is None:
            self.digit_dictionary = cathode_digit_dictionary

    def clear(self, digits=1, clear_value="_"):
        for _ in itertools.repeat(digits):
            self.output_device.send_byte(self.get_hex_value(clear_value))

        self.output_device.store_data()

    def set_values(self, values):
        hex_data = self.convert_to_hex(values)

        for data in hex_data:
            self.output_device.send_byte(data)

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
