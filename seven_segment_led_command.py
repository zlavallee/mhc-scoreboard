import logging

import RPi.GPIO as GPIO

from config import config
from gpio.seven_segment_led import create_seven_segment_led
from setup import setup_logging


def print_msg():
    print('Program is running...')
    print('Please press Ctrl+C to end the program...')


def setup():
    GPIO.setmode(GPIO.BOARD)
    setup_logging(logging.INFO)


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
        loop(create_seven_segment_led(config.get_scoreboard_config()))
    finally:
        destroy()
