#!/usr/bin/python
import sys
import time
from pygoogle import pygoogle

search_string=""
for string in sys.argv[1:]:
   search_string += " " + string

search_string = search_string.strip()

print "Searching for %s" %search_string,
for dot in range(0,5):
    #print ".",
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(1)
    if dot == 5:
        print "\n"

g=pygoogle(search_string)
g.pages=3
count=g.get_result_count()
results=g.get_urls()

print "First %s out of %s results:\n" %(len(results),count)
for result in results:
    print result

print "\n"
