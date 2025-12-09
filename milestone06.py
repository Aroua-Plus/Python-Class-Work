#!/usr/bin/env python3
"""
    Author: Kyler David
    Email: kdavid1@madisoncollege.edu
    Description: Semester-long course project script which will analyze 
    an Apache web log to determine current threats.
"""
import sys


listOfYs = ['y', 'yes', 'yep', 'yup', 'yeah']

if len(sys.argv) > 1:
    strContinue = sys.argv[1].lower()

else:
    strContinue = input("Would you  like to continue? (y/n):\n>>>> ").lower()

if strContinue in listOfYs:
    print("\nGreat! continuing with the rest of the script...\n")


    with open("06_CP-Access.log", "r") as wrapperLogFile:
        strLogLines = wrapperLogFile.read()

        listLogLines = strLogLines.split('\n')

    with open("milestone06analysis.txt", "w") as wrapperLogFile:
        for strLogLine in listLogLines:
            listLogLine =  strLogLine.split(" ")
            strIPAddress = listLogLine[0]
            strReturnCode = listLogLine[8]
            output = f"{strIPAddress} - {strReturnCode}"
            if strReturnCode >= '400':
                print(output)
                if strReturnCode >= '500':
                    wrapperLogFile.write(f"{output}\n")
   

