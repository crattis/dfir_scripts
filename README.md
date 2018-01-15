# DFIR_Scripts
Scripts (shell, python, etc), I wrote for use in different DFIR related activities. These are things I wrote to improve my scripting skills and used for scratching repetitive itches.

# Computer Ping (Python).
  This script is designed to ping a host name or ip address for up to 60 minutes, once every 10 minutes. It stops when it can either ping the box, or when the hour is up. The script will load a text file when the script completes.

There are three versions of the script, depending on the environment
 * lComputerPing.py - This is for use on GNU/Linux based systems.
 * cwComputerPing.py - For use on Windows computers with Cygwin.
 * wComputerPing.py - For Windows running Python.
 
 Linux on Windows (Ubuntu on Windows) does not appear to support ping, when this was tested.

# Base64 and Hex decoders (Python and compiled exe for Windows).
  Similar to the 2 shell scripts below, but written in python and use a file instead of a command line argument (by request).
  
  These will convert base64 or hexadecimal in the associated text file (base64.txt or hex.txt) and make it human readable. The script and input files need to stay in the same folder, output file will also be in that folder. Note on the Hex, make sure there is no line breaks or spaces. All hex strings have to be one line for the script to work.
  
  Python scripts, run like all python scripts and require python 3.6 or higher to be installed.
  
  Exe versions are fully self-contained Windows executables. Change input file’s data to what needs to be decoded, save, and double click exe. Then check the generated output file.


# HTTP Extractor (Python).
  This script is designed to take a file containing HTTP links that need to have the host information extracted for IOCs or block lists. It was originally designed to take the output of a web based tool (copied and pasted to a text file) and only show one http:// host data / for all instances in the text file. It works on fanged and de-fanged domains and ip addresses, and catches HTTP and HTTPS.

Current versions of the script, dependent upon environment
 * lHttpExtractor.py - This is for use on GNU/Linux based systems.
 * cyHttpExtractor.py - For use on Windows Computers with Cygwin.

# Shellscripts (Shell / Bourne-Again SHell)
* killSpam.sh - Works with files in SpamAssassin's quarantine folder. Shows the To, From, Date, and Subject lines, and then asks to release email to recipient or delete the email.
* b64Decode.sh - cli script to convert user supplied base64 text to ASCII
* hexDecode.bsh - cli script to convert user supplied hexadecimal to ASCII
* uHits.sh -  A quick script to take a file name from the user to sort, remove duplicates with count, and sort result. Looking for Unique Hits (uHits)
