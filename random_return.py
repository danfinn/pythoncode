#!/usr/bin/python

def check_string(string):
  if string.lower() == "true" or string.lower() == "false":
    return "Boolean"
  elif string.isdigit():
    return "Digit"
  elif string.isalnum():
    return "Alphanumeric"
  else:
    return "Sorry, that's a type I'm not familiar with"

input=raw_input("Enter a string and I will tell you what type it is : ")
print check_string(input)
