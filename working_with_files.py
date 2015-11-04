#!/usr/bin/python

buffersize = 100000

input = open('/Users/dfinn/Downloads/Configuration_of_hosts.jpg', 'rb')
output = open('/tmp/image2.jpg', 'wb')
buffer = input.read(buffersize)

#for line in input:
#  print(line, file=output, end='')

while len(buffer):
  output.write(buffer)
  print('.', end='')
  buffer = input.read(buffersize)
