#!/usr/bin/python
import pingdomlib
import socket
import time

CARBON_SERVER = '10.0.16.16'
CARBON_PORT = 2003

api = pingdomlib.Pingdom('dfinn@ea.com','password','y7lz2aipach4qlwcbefb18jh4sxt2swz')


def send_to_graphite(lasttesttime,lastresponsetime):
        message = 'pingdom.response.time %s %s \n' % (lastresponsetime,lasttesttime)
        print message
        try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((CARBON_SERVER,CARBON_PORT))
                sock.sendall(message)
        except:
                print "IOError connecting ", CARBON_SERVER
        finally:
                sock.close()

def get_and_send():
        response = api.getChecks()
        for check in response:
                lastresponsetime = check.lastresponsetime
                lasttesttime = check.lasttesttime
                send_to_graphite(lasttesttime,lastresponsetime)

while True:
        get_and_send()
        time.sleep(5)
