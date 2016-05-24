# -*- coding: utf-8 -*-
"""
Spyder Editor
I
This is a temporary script file.
"""

import csv

with (open('PJM_20160516_FLOWFEB.csv', 'r')) as inFile:
  ReadMe = csv.reader(inFile)

  names = []
  next(ReadMe)
  for row in ReadMe:
    names.append(row[0])

for name in set(names):
  outFileName = name + '.csv'
  with(open(outFileName, 'w')) as outFile:
    outWriter = csv.writer(outFile)
    with (open('PJM_20160516_FLOWFEB.csv', 'r')) as inFile:
      ReadMe = csv.reader(inFile)
      outWriter.writerow(next(ReadMe))
      for row in ReadMe:
        if row[0] == name:
          outWriter.writerow(row)
#fin





