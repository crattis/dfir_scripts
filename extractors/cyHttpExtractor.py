#! python3
#
# http_extractor.py
#
# Takes a text copy of HTTP URIs from your file and extracts and prints a
# list of ip addresses and domains.
#
# Usage: http_extractor.py <user supplied filename>
#
# Writen for python3 using Cygwin on Windows
################################################################################

# load needed modules
import sys
import re
import logging

# check for command line arguments, asks user for filename if missing.
if len(sys.argv) > 1:
    my_file_name = (sys.argv[1])
else:
    my_file_name = input("What file has the data?: ")

dom_check = []
dom_url = re.compile(r'[a-zA-Z\-\.]+:\/\/[^\/]+:?')

# Open the user provided file as read-only, build a list from the file, and
# close.
with open(my_file_name, "r") as lookup_list:
    items = lookup_list.read().splitlines()

# Get list of ip address and domains, and remove duplicates
for list_item in items:
    if dom_url.search(list_item):
        dom_match = dom_url.search(list_item)
        if dom_match.group(0) not in dom_check:
            dom_check.append(dom_match.group(0))

# print results
for dom_name in dom_check:
    logging.info(dom_name)
