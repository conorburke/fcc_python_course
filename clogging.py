from cgitb import handler
import sys
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
# logging name is set to root by default. especially in modules should rename
# good practice to rename like this:
logger = logging.getLogger(__name__)
# default level only shows warning and up
logging.basicConfig(level=logging.DEBUG)
# these two lines don't propogate the log up to the terminal, which happens by default when using getLogger above
# logger.handlers = []
logger.propagate = False
# logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
#     datefmt="%d/%b/%Y %H:%M:%S",
#     stream=sys.stdout)

# logger.debug('a debug')
# logger.info('an info')
# logger.warning('a warning')
# logger.error('an error')
# logger.critical('a critical')

# create handlers for where to log
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('log.log')

formatter = logging.Formatter(fmt="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt="%d/%b/%Y %H:%M:%S")

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.info("chaos!")

# steps
# import logging
# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.PIckone)
# logger.propagate = False
# create handler
# create formatter
# set formatter on handler
# add handlers to logger
# log!

# see logging.conf
# can create logger with properties specified
# would also import logging.config
# logging.config.fileConfig('logging.conf')
# logger = logging.getLogger('logger name in conf')
# logger is now set up
# could also set up from a dict instead of a file

rotating_handler = RotatingFileHandler('logr.log', maxBytes=80, backupCount=2)
rotating_handler.setFormatter(formatter)
logger.addHandler(rotating_handler)

for _ in range(10):
    logger.info('lets roll')

# for microservices, use this import:
# pip install pythonjsonlogger

