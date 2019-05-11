import RPi.GPIO as GPIO

from gpio_adapter import SN74HC595NOutput
from seven_segment_led import SevenSegmentLed


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
