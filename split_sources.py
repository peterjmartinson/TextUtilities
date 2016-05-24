# -*- coding: utf-8 -*-
"""
This program splits a big .csv file into several smaller ones,
named by one of the fields.

csvFileName = the file to break up
field       = field to break on, with 0 being the first field

"""
import csv

csvFileName = 'PJM_20160516_FLOWFEB.csv'
field = 0

with (open(csvFileName, 'r')) as inFile:
  ReadMe = csv.reader(inFile)

  names = []
  next(ReadMe)
  for row in ReadMe:
    names.append(row[field])

for name in set(names):
  outFileName = name + '.csv'

  with(open(outFileName, 'w')) as outFile:
    outWriter = csv.writer(outFile)

    with (open(csvFileName, 'r')) as inFile:
      ReadMe = csv.reader(inFile)
      outWriter.writerow(next(ReadMe))
      
      for row in ReadMe:
        if row[field] == name:
          outWriter.writerow(row)
#fin





