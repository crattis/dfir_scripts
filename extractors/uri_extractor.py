# http_extractor.py
#
# takes a text copy of HTTP URIs from your file and extracts and prints a
# list of IP addresses and domains.
#
# Usage: http_extractor.py <user supplied filename>
#
# Written for python3
###############################################################################

# import python modules
import sys
import re


def get_file_name():
    # check for command line arguments, asks user for filename if missing.
    if len(sys.argv) > 1:
        my_file_name = (sys.argv[1])
    else:
        my_file_name = input("What file has the data?: ")
    return my_file_name


def get_data(read_file):
    # Open the user provided file as read-only, build a list from the file, and
    # close.
    with open(read_file, "r") as lookup_list:
        items = lookup_list.read().splitlines()
    return items


def process_lines(is_regex):
    # processes the lines from the file looking for http, ftp, ldap, etc at
    # the start of the string and deduplicates items already found.
    dom_match = []
    dom_check = []
    dom_url = re.compile(r'[a-zA-Z\-\.]+:\/\/[^\/]+:?')
    for list_item in is_regex:
        if dom_url.findall(list_item):
            dom_match = dom_url.findall(list_item)
            for is_match in dom_match:
                if is_match not in dom_check:
                    dom_check.append(is_match)
    return dom_check


if __name__ == '__main__':
    work_file = get_file_name()
    work_lines = get_data(work_file)
    match_lines = process_lines(work_lines)
    for result in match_lines:
        print(result)
