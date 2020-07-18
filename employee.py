#import module
import loghelper
import logging
import traceback
import time

#logger = logging.getLogger('filelogExample')

logger = logging.getLogger('timedRotatingFileHandler')

logger.debug('from emp :: debug message')
logger.info('from emp :: info message')

for _ in range(10):
	print("timedRotatingFileHandler ")
	time.sleep(2)

def method1():
	try:
	    a = [1, 2, 3]
	    value = a[3]
	except:
	    logger.error("uncaught exception: %s", traceback.format_exc())
	    logger.exception("exception")

def method2():
	try:
	    a = [1, 2, 3]
	    value = a[3]
	except:
	    logger.error("uncaught exception 2: %s", traceback.format_exc())
	    logger.exception("exception 2")