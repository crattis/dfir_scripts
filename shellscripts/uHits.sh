#! /bin/sh
#
# A quick script to take a file name from the user to sort, remove duplicates\
# with count, and sort result. Looking for Unique Hits (uHits)
#
# Chris J
# [@]rattis
###############################################################################
sort $1 | uniq -c | sort -rn
