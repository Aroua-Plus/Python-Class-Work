#!/usr/bin/env python3
"""
    Author: Kyler David
    Email: kdavid1@madisoncollege.edu
    Description: Semester-long course project script which will analyze 
    an Apache web log to determine current threats.
"""
strUserInput = input("What is your name?\n>>>>")
strLogLine = '111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"'
listLogLine =  strLogLine.split()

print(f"Welcome,  {strUserInput}!")
print(f"Log Request from: {listLogLine[0]:*^22}")
print(f"Return Code: {listLogLine[8]}")

