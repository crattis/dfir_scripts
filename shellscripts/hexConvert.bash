#! /usr/bin/bash
#
# convert hex values to standard ASCII
#
# Chris J
# [@]rattis
###############################################################################
hexValue=$1
covAscii=`echo "$hexValue" | xxd -r -p`

echo -e "\n"
echo -e "$hexValue \t $covAscii "
echo -e "\n"
