#!/usr/bin/python

# With sshd debug logging enabled we needed a way to see which users were using legacy cbc
# ciphers.  sshd debug logs are multiline logs so parsing them with something like ELK didn't 
# seem possible.  A few lines of python (and an OS call) was able to do it pretty eaisly.

import pwd
import os

stream = os.popen("grep -i cbc -A 8 /var/log/secure*|grep userauth-request|awk '{print $10}'|grep -v root|sort|uniq")
cbc_users = stream.read().splitlines()
all_users = [u[0] for u in pwd.getpwall()]

for user in cbc_users:
    if user in all_users:
        print user
