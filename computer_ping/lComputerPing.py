#!/usr/bin/python3
# computer_ping.py a simple ping to see if a box is up or not.

# load needed modules
import logging
import os
import time
import subprocess
import sys

# check for command line arguments, ask for target if none provided.
if len(sys.argv) > 1:
    host_name = (sys.argv[1])
else:
    host_name = input("What host are you looking for? (Enter hostname or ip address):  ")


def ping_computer(ping_this):
    """Function to call Linux ping command."""
    response = os.system('ping -c 1 -W 100 ' + ping_this + ' > /dev/null 2>&1')
    return response


def alert_box(ping_result):
    """Function to open text file with the result of the final ping (up or down)."""
    file_object = open(host_name + '_ping_result.txt', 'w')
    file_object.write(host_name + ping_result)
    file_object.close()
    subprocess.Popen(['xdg-open', host_name + '_ping_result.txt'])
    # subprocess.Popen(['/usr/bin/mousepad', hostName + '_ping_result.txt'])


# try pinging the host over the course of an hour, stops when the target is up.
attempts_left = 6
attempt_number = 1

while attempts_left > 0:
    upDown = ping_computer(host_name)
    if upDown == 0:
        logging.info('Attempt ' + str(attempt_number) + ': ' + host_name + ' is up!')
        alert_box(' is up at this time!')
        break
    elif attempts_left == 1:
        logging.info('Attempt ' + str(attempt_number) + ': ' + host_name + ' is down! Ping attempts ended')
        alert_box(' is down at this time! Tried for 1 hour.')
    else:
        logging.info('Attempt ' + str(attempt_number) + ': ' + host_name + ' is down, trying again in 10 minutes.')
        time.sleep(600)
    attempt_number += 1
    attempts_left -= 1
# sleep 3 seconds to allow system to open text file, before deleting text file.    
time.sleep(3)
os.remove(host_name + '_ping_result.txt')
