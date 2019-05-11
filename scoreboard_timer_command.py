import RPi.GPIO as GPIO

from gpio_adapter import SN74HC595NOutput
from scoreboard_timer import ScoreboardTimer


def print_msg():
    print('Program is running...')
    print('Please press Ctrl+C to end the program...')


def setup():
    GPIO.setmode(GPIO.BOARD)


def destroy():
    GPIO.cleanup()


def loop(scoreboard_timer):
    commands = {
        'start': lambda _: scoreboard_timer.start(),
        'stop': lambda _: scoreboard_timer.stop(),
        'reset': lambda _: scoreboard_timer.reset()
    }

    while True:

        value = input('Enter command:')
        command = commands[value]

        if command is None:
            print('Unknown command: {}'.format(value))
            print('Available commands: {}'.format(list(' ,'.join(commands.keys()))))
        else:
            command()


if __name__ == '__main__':
    print_msg()
    setup()
    try:
        timer = ScoreboardTimer(SN74HC595NOutput())
        timer.start()
        loop(timer)
    finally:
        destroy()
