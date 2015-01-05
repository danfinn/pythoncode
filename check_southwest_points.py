#!/usr/bin/python
# basic python script to check the current points for backcountry.com on the Southwest shopping portal
import urllib
import re

site = urllib.urlopen("https://rapidrewardsshopping.southwest.com/me____.htm?keywords=backcountry.com&mnpos=1844|8925|1|1|search_box&gmid=2031")
site.response = site.read()
#print site.response
#print site.read()
#regex = re.compile("backcountry.com\&tot\=1\&r\=(\d+)pts",re.IGNORECASE)
#r = regex.search(site.response)
#print (r.groups())
#print r


m = re.search("backcountry.com\&tot\=1\&r\=(\d+)pts",site.response,re.IGNORECASE)
if m:
   # positive match
   #print("match:",m.group(1))
   print "Currently bc.com is at %s points." %m.group(1)
else:
   print "Something went wrong, unable to find current bc.com points."
