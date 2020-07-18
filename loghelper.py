# Then use the config file in the code
import logging
import logging.config


logging.config.fileConfig('logging.conf')

# create logger with the name from the config file. 
# This logger now has StreamHandler with DEBUG Level and the specified format
logger = logging.getLogger('filelogExample')

logger.debug('from loghelper :: debug message')
logger.info('from loghelper :: info message')