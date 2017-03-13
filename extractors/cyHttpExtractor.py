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

# laod needed modules
import sys
import re

#check for command line arguments, asks user for filename if missing. 
if len(sys.argv) > 1:
	myFileName = (sys.argv[1])
else: 
	myFileName = input("What file has the data?: ")

dom_check = []
dom_url = re.compile(r'https?:\/\/[^\/]+:?')

# Open the user provided file as read-only, build a list from the file, and
# close.
with open(myFileName, "r") as lookup_list:
    items = lookup_list.read().splitlines()

# Get list of ip address and domains, and remove duplicates
for list_item in items:
    if dom_url.search(list_item):
        dom_match = dom_url.search(list_item)
        if dom_match.group(0) not in dom_check:
            dom_check.append(dom_match.group(0))

# print results
print()
for dom_name in dom_check:
    print(dom_name)
