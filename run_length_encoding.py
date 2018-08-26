#!/usr/bin/python
from collections import OrderedDict

input = raw_input("Please enter in some text to be compressed: ")

def runlengthencode(input):
  dict=OrderedDict.fromkeys(input,0)

  for char in input:
    dict[char] += 1

  output=''
  for k,v in dict.iteritems():
    output = output + k + str(v)
  return output

print runlengthencode(input)
