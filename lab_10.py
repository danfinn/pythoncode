#!/usr/bin/python

class LogMessage:
  def __init__(self,filename):
    self.filename = filename

  def read(self):
    input = open(self.filename, 'r')
    for line in input:
      print(line, end='')

  def write(self,error):
    output = open(self.filename, 'a')
    output.write(error)
    
error_logging = LogMessage('/tmp/blah.txt')
error_logging.read()
error_logging.write('broken')
