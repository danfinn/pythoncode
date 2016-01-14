#!/usr/bin/python

import sqlite3

class LogMessageDB:
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

class LogMessageFile:
  def __init__(self,filename):
    self.filename = filename

  def read(self):
    input = open(self.filename, 'r')
    for line in input:
      print(line)
      #print(line, end='')

  def write(self,error):
    output = open(self.filename, 'a')
    output.write(error)
