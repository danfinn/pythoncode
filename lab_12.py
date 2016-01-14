#!/usr/bin/python

# loads mobule from another file

#from lab_12_log_module import LogMessageDB

#error_logging = LogMessageDB('/tmp/error_log.db')
#error_logging.write('this is an error log from lab 12')
#error_logging.read()

from lab_12_log_module import LogMessageFile

error_logging = LogMessageFile('/tmp/error_log.txt')
error_logging.write('this is an error log from lab 12')
error_logging.read()
