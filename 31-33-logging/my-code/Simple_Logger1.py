from logbook import Logger, StreamHandler
import sys

StreamHandler(sys.stdout).push_application()
log = Logger('Logbook')
log.info('Hello World')