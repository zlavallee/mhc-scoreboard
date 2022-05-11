import logging


def setup_logging(level=logging.INFO):
    logging.getLogger().setLevel(level)
    logging.basicConfig(
        format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
        level=level,
        datefmt='%Y-%m-%d %H:%M:%S')


def destroy():
    try:
        import RPi.GPIO as GPIO
    except ImportError:
        raise NotImplementedError("You need the bandana package to wear hats")
    else:
        GPIO.cleanup()


def initialize():
    try:
        import RPi.GPIO as GPIO
    except ImportError:
        raise NotImplementedError("You need the bandana package to wear hats")
    else:
        GPIO.setmode(GPIO.BOARD)
