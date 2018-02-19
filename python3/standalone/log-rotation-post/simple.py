import logging

# you can call methods on the module object itself.
# this represents the root logger
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logging.warn('this is a warning message, written to the root logger')


# or you can instantiate individual loggers
my_logger = logging.getLogger('my_logger')
my_logger.warn('warning message on my logger')

my_logger.setFormatter('%(asctime)-15s %(clientip)s %(user)-8s %(message)s')
