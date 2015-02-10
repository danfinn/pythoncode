#!/usr/bin/python
# used to change the MAXIS_ENV environment variable which is used by various other apps

import os
import re
import sys
import fileinput

if (len(sys.argv) < 2):
        print "You must give a new environment name"
        sys.exit()
else:
        new_env=sys.argv[1]

def get_current_env():
        # Use regex to determine what MAXIS_ENV is currently set to
        etc_profile=open("/etc/profile","r")
        regex=re.compile('MAXIS_ENV=(\w+)')
        for line in etc_profile:
                env=regex.findall(line)
        #etc_profile.close()
        #print 'MAXIS_ENV is currently set to "%s"' % env[0]
        return env[0]

def update_file(file,current_env,new_env):
        # Check if file exists
        if not os.path.isfile(file):
                print "Error on replacing text, %s is not a regular file" % file

        # Open current file for reading
        current_file=open(file,'r').read()
        # Also open a file handle on the same file for writing
        new_file=open(file,'w')
        # Search and replace 
        changed_data=current_file.replace(current_env,new_env)
        # Write out the changed data to the file
        new_file.write(changed_data)
        #current_file.close()
        new_file.close()
        current_env=get_current_env()
        print 'MAXIS_ENV in %s has been changed to "%s"' % (file,current_env)


current_env=get_current_env()
print ""
print 'Currently MAXIX_ENV is set to "%s"' % current_env
update_file("/etc/profile",current_env,new_env)
update_file("/usr/bin/maxisenv",current_env,new_env)
print ""
