# -*- coding: utf-8 -*-
"""
This program renames elements of a field in a .csv file with 
letters of the alphabet.

csvFileName = the file to parse
field       = the field to rename

"""
import csv

csvFileName = 'PJM_20160516_FLOWFEB.csv'

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dummy = list(alphabet)

with (open(csvFileName, 'r')) as inFile:
  ReadMe = csv.reader(inFile)

  names = []
  next(ReadMe)
  for row in ReadMe:
    names.append(row[field])

with (open(csvFileName, 'r')) as inFile:
  ReadMe = csv.reader(inFile)
  outFileName = csvFileName + '_renamed.csv'
  with (open(outFileName, 'w')) as outFile:
    outWriter = csv.writer(outFile)
    outWriter.writerow(next(ReadMe))
    
    for row in ReadMe:
      next(row)
      tempArray = []
      for element in row:
        tempArray[  ######## not sure how to do this
        # make an array with element 0 the Alphabet letter
        # subsequent element the rest of ReadMe's row
        # outWriter.writerow(that array)
        # increment the Alphabet index
        # repeat until the end of ReadMe
    
"""
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
"""

#fin





