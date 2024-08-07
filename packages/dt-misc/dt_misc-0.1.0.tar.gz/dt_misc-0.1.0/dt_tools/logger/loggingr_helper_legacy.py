import sys
# import logging
from dt_tools.logging.logging_helper import logger_wraps as lw

DEFAULT_FILE_LOGFMT = "<green>{time:MM/DD/YY HH:mm:ss}</green> |<level>{level: <8}</level>|<cyan>{name:10}</cyan>|<cyan>{line:3}</cyan>| <level>{message}</level>"
DEFAULT_CONSOLE_LOGFMT = "<level>{message}</level>"

# TODO:
#   - Loglevels - TRACE, DEBUG, INFO, ERROR, CRITICAL

def configure_logger(log_target = sys.stderr, log_level: str = "INFO", log_format: str = None, **kwargs) -> int:
    """
    Configure logger via python logging.

    Parameters:
        log_target: defaults to stderr, but can supply filename as well
        log_level : TRACE|DEBUG|INFO(dflt)|ERROR|CRITICAL
        log_format: format for output log line
        other     : keyword args related to loguru logger.add() function

    Returns:
        logger_handle_id: integer representing logger handle
    """
    # TODO: implement
    pass

def logger_wraps(args, entry=True, exit=True, level="DEBUG"):
    """
    function decorator wrapper to log entry and exit
    
    Example::
        @logger_wraps()
        def foo(a, b, c):
            logger.info("Inside the function")
            return a * b * c 

    """    
    lw(*args, entry=entry, exit=exit, level=level)

