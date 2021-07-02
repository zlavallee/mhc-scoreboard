import RPi.GPIO as GPIO

from gpio import scoreboard_timer


def print_msg():
    print('Program is running...')
    print('Please press Ctrl+C to end the program...')


def setup():
    GPIO.setmode(GPIO.BOARD)


def destroy():
    GPIO.cleanup()


def loop(timer):
    commands = {
        'start': lambda: timer.start(),
        'stop': lambda: timer.stop(),
        'reset': lambda: timer.reset()
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
        loop(scoreboard_timer.create_scoreboard_timer())
    finally:
        destroy()
