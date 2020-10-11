# Simple python script for parsing Apache log
Script can get top of IP's that appear in log and print list of user-agent from selected IP. This may help to find unwanted crawlers or scrappers. 

##Requirements:
1. Apache log file downloaded from your server

##Instructions:
1. Put decompressed file with mask name "\*access.log*" in script folder.
2. Run "main.py".
3. Enter IP to search for user-agent.
4. Result will be printed to the Python console.

##Notice:
- only first found "access.log" file analyzed
