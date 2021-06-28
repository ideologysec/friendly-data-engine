#! /usr/bin/env python3

import csv, os
from bs4 import BeautifulSoup
from datetime import datetime

dtString = datetime.now().strftime("%Y-%m-%d-%H%M")
currentPath = os.path.abspath(os.getcwd())
candidateFile = [f for f in os.listdir(currentPath) if f.endswith('.xml')][0]

with open(candidateFile, "r") as labfile, open('{0} labdata.csv'.format(dtString), "w") as convertedData:

    csvwriter = csv.writer(convertedData)
    headingRow = ['Date', 'Type', 'Test', 'Units', 'Lower Limit', 'Upper Limit', 'Result', 'Flag', 'Comments', 'Status', 'Ordered By', 'Specimen Source', 'Lab Address']
    csvwriter.writerow(headingRow)

    soup = BeautifulSoup(labfile, 'lxml')
    table = soup.find_all('table')[9]
    tableRows = table.find_all('tr')

    for tr in tableRows:
        tableData = tr.find_all('td')
        row = [item.text for item in tableData]
        csvwriter.writerow(row)