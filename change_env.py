#!/usr/bin/python
# used to change the MAXIS_ENV environment variable which is used by various other apps

import os
import re
import sys

def get_current_env():
        # Use regex to determine what MAXIS_ENV is currently set to
        etc_profile=open("/etc/profile","r")
        regex=re.compile('MAXIS_ENV=(\w+)$')
        for line in etc_profile:
                env=regex.findall(line)
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
        full_current_env="export MAXIS_ENV=" + current_env
        full_new_env="export MAXIS_ENV=" + new_env
        changed_data=current_file.replace(full_current_env,full_new_env)
        # Write out the changed data to the file
        new_file.write(changed_data)
        #current_file.close()
        new_file.close()
        current_env=get_current_env()
        print 'MAXIS_ENV in %s has been changed to "%s"' % (file,current_env)

def usage():
        print ' ---------------------------------------------------------------------------'
        print ''
        print ' This script is used to change the environment settings to your particular '
        print ' needs.  By default, any instances built from this AMI are named "standard".'
        print ' Using this script you can change it to whatever is needed or desired.'
        print ' '
        print ' Usage : ./change_env.py newEnvironmentName'
        print ' '
        print ' '
        print ' ---------------------------------------------------------------------------'
        print ' '

def main(new_env):
        current_env=get_current_env()
        print ""
        print " ---------------------------------------------------------------------------"
        print ""
        print 'Currently MAXIX_ENV is set to "%s"' % current_env
        print ""
        update_file("/etc/profile",current_env,new_env)
        update_file("/usr/bin/maxisenv",current_env,new_env)
        print ""
        print " ---------------------------------------------------------------------------"
        print ""


if (len(sys.argv) < 2):
        usage()
else:
        new_env=sys.argv[1]
        main(new_env)
