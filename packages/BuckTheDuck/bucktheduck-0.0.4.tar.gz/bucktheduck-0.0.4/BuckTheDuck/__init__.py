import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('buck_the_duck')


def get_logger():
    return logger


def set_logger_level(log_level=logging.DEBUG):
    logger.setLevel(log_level)
