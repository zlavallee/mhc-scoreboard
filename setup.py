import logging


def setup_logging(level=logging.INFO):
    logging.getLogger().setLevel(level)
    logging.basicConfig(
        format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
        level=level,
        datefmt='%Y-%m-%d %H:%M:%S')
