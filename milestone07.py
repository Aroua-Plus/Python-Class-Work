#!/usr/bin/env python3
"""
    Author: Kyler David
    Email: kdavid1@madisoncollege.edu
    Description: Semester-long course project script which will analyze 
    an Apache web log to determine current threats.
"""
import sys


yes_responses = ["y", "yes", "yep", "yup", "yeah"]

if len(sys.argv) > 1:
    strContinue = sys.argv[1].lower()

else:
    strContinue = input("Would you  like to continue? (y/n):\n>>>> ").lower()

if strContinue.lower() in yes_responses:
    print("\nGreat! continuing with the rest of the script...\n")


    with open("06_CP-Access.log", "r") as wrapperLogFile:
        strLogLines = wrapperLogFile.read()

    listLogLines = strLogLines.split('\n')

    dictLogSummary = {}

    for strLogLine in listLogLines:
        listLogLine =  strLogLine.split(" ")
        strIPAddress = listLogLine[0]
        strReturnCode = listLogLine[8]
        output = f"{strIPAddress} - {strReturnCode}"
        if strReturnCode >= '400':
            print(output)
            
        if strIPAddress in dictLogSummary:
            dictLogSummary[strIPAddress] += 1
        else:
            dictLogSummary[strIPAddress] = 1
    with open("milestone07analysis.csv", "w") as wrapperIPCountFile:
        wrapperIPCountFile.write(f"IP,hits\n")
        for strKeyIP, intValueCount in dictLogSummary.items():
            if intValueCount >= 5:
                wrapperIPCountFile.write(f"{strKeyIP},{intValueCount}\n")


        

