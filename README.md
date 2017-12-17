# DFIR_Scripts
Scripts (shell, python, etc), I wrote for use in different DFIR related activities. These are things I wrote to improve my scripting skills and used for scratching repeditive itches.

# Computer Ping (Python).
  This script is designed to ping a host name or ip address for up to 60 minutes, once every 10 minutes. It stops when it can either ping the box, or when the hour is up. The script will load a text file when the script completes.

There are three versions of the script, depending on the environment
 * lComputerPing.py - This is for use on GNU/Linux based systems.
 * cwComputerPing.py - For use on Windows computers with Cygwin.
 * wComputerPing.py - For Windows running Python.
 
 Linux on Windows (Ubuntu on Windows) does not appear to support ping, when this was tested.

# HTTP Extractor (Python).
  This script is designed to take a file containing HTTP links that need to have the host information extracted for IOCs or block lists. It was originally desinged to take the output of a web based tool (copied and pasted to a text file) and only show one http:// host data / for all instances in the text file. It works on fanged and de-fanged domains and ip addresses, and catches HTTP and HTTPS.

Current versions of the script, dependant upon environment
 * lHttpExtractor.py - This is for use on GNU/Linux based systems.
 * cyHttpExtractor.py - For use on Windows Computers with Cygwin.

# killSpam.sh (Shell Script for Linux)
Works with files in SpamAssassin's quarantine folder. Shows the To, From, Date, and Subject lines, and then asks to release email to recipient or delete the email. 
