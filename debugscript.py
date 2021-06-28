#! /usr/bin/env python3

import csv
from bs4 import BeautifulSoup
from datetime import datetime

dtString = datetime.now().strftime("%Y-%m-%d-%H%M")

with open("labdata.xml", "r") as debugFile:
    debugSoup = BeautifulSoup(debugFile, 'lxml')
    debugTable = debugSoup.find_all('table')
    i = 0
    for item in debugTable:
        print ("\n\n")
        print ("\n####TABLE HEADING######")
        print("Current table number is:", i)
        print("Contens of table are:\n")
        print (debugTable[i])
        i=i+1
