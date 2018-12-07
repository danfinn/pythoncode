__virtualname__ = 'mysql_host'
__author__ = "Dan Finn"
__version__ = "0.2"

import os
from operator import itemgetter
from collections import OrderedDict
from salt.exceptions import (
    SaltInvocationError,
    CommandExecutionError,
)

'''
This module returns a list of hosts and their number of connections to a MySQL server

You run it like so:

salt ps-dev-db01.plansourcedev.com mysql_host.count
'''

def __virtual__():
    return True

def is_mysql_running():
    mysql_sock_file='/var/run/mysqld/mysqld.sock'
    if not os.path.exists(mysql_sock_file):
      print "MySQL does not appear to be running on this server"
      exit()

def count():
    is_mysql_running()

    output = __salt__['cmd.run']("mysqladmin --defaults-file=/root/.my.cnf proc |awk -F'|' '/Sleep|Query/ && !/localhost/{print $4}'|cut -d: -f1",python_shell=True).splitlines()

    host_totals = {}
    return_output = []
    for host in output:
      host_totals[host] = host_totals.get(host, 0) + 1

    sorted_host_totals = OrderedDict(sorted(host_totals.items(), key=itemgetter(1)))
    for host,num in sorted_host_totals.items():
      return_output.append(str(host)+' : '+str(num))
    return return_output
