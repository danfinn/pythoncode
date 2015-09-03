#!/usr/bin/python

auth=raw_input("Enter your api id and key:")

id,key=auth.split(':')

if id.isdigit() and len(id) == 14 and len(key) > 10 and len(key) < 20:
  print 'All is good'
else:
  print 'Sorry, your id and key did not meet the requirements'
