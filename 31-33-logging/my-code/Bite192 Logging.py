import logging
from typing import Callable

'''
LOG_LEVEL = {
    DEBUG : "debug",
    INFO : "info",
    WARNING : "warning",
    ERROR : "error",
    CRITICAL : "critical"
    }
'''
DEBUG = "debug"
INFO = "info"
# WARNING = "warning",
# ERROR = "error",
# CRITICAL = "critical"


def log_it(level: Callable, msg: str) -> None:
    value = callable(level)
    print(value)
    # level = logging.value
    logger = logging.getLogger()
    print(logger.setLevel(value))
    #return logging.basicConfig(
    #    filename='pybites_logger.log',
    #    level=logger().setLevel(value),
    #    format='%(msg)s:%(value)s:'
    #    )
        

if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    # log_it(INFO, "This is an info message.")
    # log_it(WARNING, "This is a warning message.")
    # log_it(ERROR, "This is an error message.")
    # log_it(CRITICAL, "This is a critical message.")