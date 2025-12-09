#!/usr/bin/env python3
"""
    Author: Kyler David
    Email: kdavid1@madisoncollege.edu
    Description: Semester-long course project script which will analyze 
    an Apache web log to determine current threats.
"""

import subprocess, argparse, requests, json

def ipLookup(inIpAddress):
    URL = f"http://ipinfo.io/{inIpAddress}/json"
    print(URL)
    return requests.get(URL).text

    

def ipAddressCount(inApacheLogFileName):

    strLinuxCmd = f"cat {inApacheLogFileName} | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5"
    completeProcess = subprocess.run(strLinuxCmd, shell=True, capture_output=True, text=True)
    return completeProcess.stdout

def main():

    parser = argparse.ArgumentParser(description="supplies input and output file names")
    parser.add_argument("-i", "--inputfilename", required=True, help="Input Apache log file name (e.g., 06_CP-Access.log)")
    parser.add_argument("-o", "--outputfilename", help="Optional output file name (e.g., analysis.txt)")
    args = parser.parse_args()

    strLinuxCmdResults = ipAddressCount(args.inputfilename)
    strHighestHittingIP = strLinuxCmdResults.split()[-1]
    print(strHighestHittingIP)

    strJSONResponse = ipLookup(strHighestHittingIP)
    dictIPInfo = json.loads(strJSONResponse)
 
    print(f". Organization: {dictIPInfo.get('org', 'N/A')}")
    print(f". City, Region: {dictIPInfo.get('city', 'N/A')}, {dictIPInfo.get('region', 'N/A')}")

    
    if args.outputfilename:
        with open(args.outputfilename, "w") as wrapperIPCountFile:
            wrapperIPCountFile.write(strLinuxCmdResults)

if __name__ == "__main__":
    main()


         

