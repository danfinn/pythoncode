#!/usr/bin/python

# Takes some sample syslog data and counts the number of times 
# a log entry was created for each minute timestamp

file = open('sample_log.txt', 'r')
count = {}

for line in file:
	datestamp = line[:12]
	if not datestamp in count:
		count[datestamp] = 1
	else:
		count[datestamp] += 1

print('Datestamp{: >9}'.format('Count'))
for k,v in count.items():
	print(k, v)
