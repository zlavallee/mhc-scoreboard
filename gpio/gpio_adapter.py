import logging

import RPi.GPIO as GPIO

from gpio.clock import create_sleep_clock
from gpio.core import ShiftRegister


class SN74HC595NOutput(ShiftRegister):
    def __init__(self, clock_speed=0.001, serial_data_input=11, memory_clock=12, serial_clock=13):
        self.SDI = serial_data_input
        self.RCLK = memory_clock
        self.SRCLK = serial_clock
        self.clock_speed = clock_speed
        self.clock = create_sleep_clock(self.clock_speed)

        GPIO.setup(self.SDI, GPIO.OUT)
        GPIO.setup(self.RCLK, GPIO.OUT)
        GPIO.setup(self.SRCLK, GPIO.OUT)
        GPIO.output(self.SDI, GPIO.LOW)
        GPIO.output(self.RCLK, GPIO.LOW)
        GPIO.output(self.SRCLK, GPIO.LOW)

    def send_byte(self, data):
        logging.debug('Sending data: {}'.format(data))
        for bit in range(0, 8):
            logging.debug('Sending bit: {}'.format(0x80 & (data << bit)))
            GPIO.output(self.SDI, 0x80 & (data << bit))
            GPIO.output(self.SRCLK, GPIO.HIGH)
            self.__tick()
            GPIO.output(self.SRCLK, GPIO.LOW)

    def store_data(self):
        GPIO.output(self.RCLK, GPIO.HIGH)
        self.__tick()
        GPIO.output(self.RCLK, GPIO.LOW)

    def __tick(self):
        self.clock.tick()
