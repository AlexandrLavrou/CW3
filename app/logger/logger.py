import logging


def logging_it():

    """logger DEBUG"""

    logger = logging.getLogger("basic")
    logger.setLevel("DEBUG")

    file_handler = logging.FileHandler("logs/debug.log", encoding="utf-8")
    logger.addHandler(file_handler)

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler.setFormatter(formatter)

    """logger INFO"""

    logger_api = logging.getLogger("api")
    logger_api.setLevel("INFO")

    file_handler_api = logging.FileHandler("logs/api.log", encoding="utf-8")
    logger_api.addHandler(file_handler_api)

    formatter_api = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler_api.setFormatter(formatter_api)

    return logger

