import time

import RPi.GPIO as GPIO

from seven_segment_led import SevenSegmentLed


class SN74HC595NOutput:
    def __init__(self, clock_speed=0.001, serial_data_input=11, memory_clock=12, serial_clock=13):
        self.SDI = serial_data_input
        self.RCLK = memory_clock
        self.SRCLK = serial_clock
        self.clock_speed = clock_speed

        GPIO.setup(self.SDI, GPIO.OUT)
        GPIO.setup(self.RCLK, GPIO.OUT)
        GPIO.setup(self.SRCLK, GPIO.OUT)
        GPIO.output(self.SDI, GPIO.LOW)
        GPIO.output(self.RCLK, GPIO.LOW)
        GPIO.output(self.SRCLK, GPIO.LOW)

    def send_byte(self, data):
        for bit in range(0, 8):
            GPIO.output(self.SDI, 0x80 & (data << bit))
            GPIO.output(self.SRCLK, GPIO.HIGH)
            self.__tick()
            GPIO.output(self.SRCLK, GPIO.LOW)

    def store_data(self):
        GPIO.output(self.RCLK, GPIO.HIGH)
        self.__tick()
        GPIO.output(self.RCLK, GPIO.LOW)

    def __tick(self):
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
        value = input('Enter number from 0-99 to display:')
        display.set_values(value)


if __name__ == '__main__':  # Program starting from here
    print_msg()
    setup()
    try:
        loop(SevenSegmentLed(SN74HC595NOutput()))
    finally:
        destroy()
