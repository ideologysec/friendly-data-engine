#! /usr/bin/env python3

import os
from bs4 import BeautifulSoup
from datetime import datetime

dtString = datetime.now().strftime("%Y-%m-%d-%H%M")

currentPath = os.path.abspath(os.getcwd())
candidateFile = [f for f in os.listdir(currentPath) if f.endswith('.xml')][0]
files = [f for f in os.listdir(currentPath) if f.endswith('.xml')]

print(candidateFile)

for file in files:
    fullPath = os.path.join(currentPath, file)
    print(fullPath)
    if os.path.isfile(fullPath):
        lastModDate = datetime.fromtimestamp(os.path.getmtime(fullPath))
    else:
        lastModDate = datetime.fromtimestamp(0)
    print ("Lastmod date is:", lastModDate)


with open(candidateFile, "r") as debugFile:
    print("Found and opened the right file; filename is: ", candidateFile)

    # debugSoup = BeautifulSoup(debugFile, 'lxml')
    # debugTable = debugSoup.find_all('table')

    # specificTable = debugTable[9]
    # tableRows = specificTable.find_all('tr')
    # print(tableRows)

    # print every table in the file (some interesting possibilities here!)
    # i = 0
    # for item in debugTable:
    #     print ("\n\n")
    #     print ("\n####TABLE HEADING######")
    #     print("Current table number is:", i)
    #     print("Contens of table are:\n")
    #     print (debugTable[i])
    #     i=i+1

