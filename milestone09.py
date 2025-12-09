#!/usr/bin/env python3
"""
    Author: Kyler David
    Email: kdavid1@madisoncollege.edu
    Description: Semester-long course project script which will analyze 
    an Apache web log to determine current threats.
"""
import sys
def parseLogEntry(inStrLogLine):
    listLogLine =  inStrLogLine.split(" ")
    strIPAddress = listLogLine[0]
    strReturnCode = listLogLine[8]
    return strIPAddress, strReturnCode

def main():

    yes_responses = ["y", "yes", "yep", "yup", "yeah"]

    if len(sys.argv) > 1:
        strContinue = sys.argv[1].lower()
    else:
        strContinue = input("Would you  like to continue? (y/n):\n>>>> ").lower()

    if strContinue.lower() in yes_responses:

        with open("06_CP-Access.log", "r") as wrapperLogFile:
            strLogLines = wrapperLogFile.read()

        listLogLines = strLogLines.split('\n')

        dictLogSummary = {}

        for strLogLine in listLogLines:
            strIPAddress, strReturnCode = parseLogEntry(strLogLine)
            strIPReturnCode = f"{strIPAddress} - {strReturnCode}"
            if strReturnCode >= '400':
                print(strIPReturnCode)
               
            if strIPAddress in dictLogSummary:
                dictLogSummary[strIPAddress] += 1
            else:
                dictLogSummary[strIPAddress] = 1

        with open("milestone07analysis.csv", "w") as wrapperIPCountFile:
            wrapperIPCountFile.write(f"IP,hits\n")
            for strKeyIP, intValueCount in dictLogSummary.items():
                if intValueCount >= 5:
                    wrapperIPCountFile.write(f"{strKeyIP},{intValueCount}\n")
if __name__ == "__main__":
    main()


         

