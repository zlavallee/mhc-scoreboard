import logging

import RPi.GPIO as GPIO

from config import config
from gpio.seven_segment_led import create_seven_segment_led


def print_msg():
    print('Program is running...')
    print('Please press Ctrl+C to end the program...')


def setup():
    GPIO.setmode(GPIO.BOARD)
    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')


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
