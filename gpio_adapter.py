import RPi.GPIO as GPIO
import time


class SevenSegmentLed:
    cathode_digit_dictionary = {
        0: 0x3F,
        1: 0x06,
        2: 0x5B,
        3: 0x4F,
        4: 0x66,
        5: 0x6D,
        6: 0x7D,
        7: 0x07,
        8: 0x7F,
        9: 0x67,
    }

    anode_digit_dictionary = {
        0: 0xC0,
        1: 0xF9,
        2: 0xA4,
        3: 0xB0,
        4: 0x99,
        5: 0x92,
        6: 0x82,
        7: 0xF8,
        8: 0x80,
        9: 0x98,
    }

    def __init__(self, clock_speed=0.001, serial_data_input=11, memory_clock=12, serial_clock=13,
                 digit_dictionary=None):

        self.SDI = serial_data_input
        self.RCLK = memory_clock
        self.SRCLK = serial_clock
        self.clock_speed = clock_speed
        self.digit_dictionary = digit_dictionary

        if digit_dictionary is None:
            self.digit_dictionary = self.cathode_digit_dictionary

        GPIO.setup(self.SDI, GPIO.OUT)
        GPIO.setup(self.RCLK, GPIO.OUT)
        GPIO.setup(self.SRCLK, GPIO.OUT)
        GPIO.output(self.SDI, GPIO.LOW)
        GPIO.output(self.RCLK, GPIO.LOW)
        GPIO.output(self.SRCLK, GPIO.LOW)

    def set_number(self, number):
        ones_digit, tens_digit = self.convert_to_hex(number)

        self.hc595_in(tens_digit)
        self.hc595_in(ones_digit)
        self.hc595_out()

    def convert_to_hex(self, number):
        string_number = str(number)

        ones_digit = self.digit_dictionary[int(string_number[0])]
        tens_digit = self.digit_dictionary[int(string_number[1])]

        return tens_digit, ones_digit

    def hc595_in(self, data):
        for bit in range(0, 8):
            GPIO.output(self.SDI, 0x80 & (data << bit))
            GPIO.output(self.SRCLK, GPIO.HIGH)
            self.tick()
            GPIO.output(self.SRCLK, GPIO.LOW)

    def hc595_out(self):
        GPIO.output(self.RCLK, GPIO.HIGH)
        self.tick()
        GPIO.output(self.RCLK, GPIO.LOW)

    def tick(self):
        time.sleep(self.clock_speed)


def print_msg():
    print('Program is running...')
    print('Please press Ctrl+C to end the program...')


def setup():
    GPIO.setmode(GPIO.BOARD)


def destroy():
    GPIO.cleanup()


def loop(display):
    while True:
        value = input('Enter two digit number to display:')
        display.set_number(value)


if __name__ == '__main__':  # Program starting from here
    print_msg()
    setup()
    try:
        loop(SevenSegmentLed())
    except KeyboardInterrupt:
        destroy()
