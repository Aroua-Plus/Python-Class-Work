#!/usr/bin/env python3
"""
    Author: Kyler David
    Email: kdavid1@madisoncollege.edu
    Description: Semester-long course project script which will analyze 
    an Apache web log to determine current threats.
"""
import sys
import subprocess

def ipAddressCount(inApacheLogFileName):
    strLinuxCmd = f"cat {inApacheLogFileName} | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5"
    completeProcess = subprocess.run(strLinuxCmd, shell=True, capture_output=True, text=True)
    return completeProcess.stdout

# Not used in this script, but is being savedd as utility for other scripts
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
        strLinuxCmdResults = ipAddressCount("06_CP-Access.log")
        print(strLinuxCmdResults)
        with open("milestone10analysis.txt", "w") as wrapperIPCountFile:
            wrapperIPCountFile.write(strLinuxCmdResults)
if __name__ == "__main__":
    main()


         

