#!/usr/bin/python

import sqlite3

class LogMessage:
  def __init__(self,database):
    self.database = database
    self.db = sqlite3.connect(self.database)
    self.db.execute('create table if not exists LogMessage(error_message text)')
    self.db.commit()
    self.db.close()

  def read(self):
    self.db = sqlite3.connect(self.database)
    input = self.db.execute('select * from LogMessage')
    for line in input:
      print(line)
    self.db.close()

  def write(self,error):
    self.db = sqlite3.connect(self.database)
    self.db.execute('insert into LogMessage (error_message)values(?)', (error,))
    self.db.commit()
    self.db.close()
    
error_logging = LogMessage('/tmp/error_log.db')
error_logging.write('this is an error message')
error_logging.read()
