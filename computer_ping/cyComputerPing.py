#! python3
# computer_ping.py a sinple ping to see if a box is up or not.
# This version is for Windows running Python under Cygwin.

# load needed libraries
import logging
import os
import time
import subprocess
import sys

# TODO make all these ping python files into a callable modular function.
# check for command line arguments, ask for target if none provided.
if len(sys.argv) > 1:
    host_name = (sys.argv[1])
else:
    host_name = input("What host are you looking for? (Enter hostname or ip address):  ")


def ping_computer(ping_this):
    """Function to call windows ping."""
    response = os.system('ping -n 1 -w 100 ' + ping_this + ' > /dev/null 2>&1')
    return response


def alert_box(ping_result):
    """Function to open Notepad.exe with the result of final ping (Up or Down)"""
    file_object = open(host_name + '_ping_result.txt', 'w')
    file_object.write(host_name + ping_result)
    file_object.close()
    subprocess.Popen(['notepad.exe', host_name + '_ping_result.txt'])


# try pinging the host over the course of an hour, stops when the target is up.
attempts_left = 6
attempt_number = 1

while attempts_left > 0:
    up_down = ping_computer(host_name)
    if up_down == 0:
        # TODO make these 3 statements into a function you can pass the last string parameter through.
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
# sleep 5 seconds to allow Operating System to open the file, then remove file.
time.sleep(5)
os.remove(host_name + '_ping_result.txt')
