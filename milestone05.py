#!/usr/bin/env python3
"""
    Author: Kyler David
    Email: kdavid1@madisoncollege.edu
    Description: Semester-long course project script which will analyze 
    an Apache web log to determine current threats.
"""

with open("05_CP-Access.log", "r") as wrapperLogFile:
    strLogLines = wrapperLogFile.read()

    listLogLines = strLogLines.split('\n')

with open("milestone05analysis.txt", "w") as wrapperLogFile:
    for strLogLine in listLogLines:
        listLogLine =  strLogLine.split(" ")
        if len(listLogLine) > 8:
            output = f"{listLogLine[0]} - {listLogLine[8]}"
            
            print(output)
            wrapperLogFile.write(f"{output}\n")
    
   

