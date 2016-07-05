"""
In:     An external file that contains a list of ICD-9/ICD-10 codes
Out:    A list of all possible unique variations of those codes
Author: Peter Martinson
Date:   June 8, 2016
"""

import math
# import textwrap
import re

print("This program requires an external file that contains a list of ICD-9/ICD-10 codes.")
print("The file must have one code per line, no commas or spaces:")
print("-----")
print("37.0")
print("102.00")
print("M37.8")
print("etc.")
print("-----")

# variable declarations
inputFileName = input("Name of file with the codes: ")
codes = []
parsedCodes = []
outCode = ''
i = 0

# function definition
def parseCode(n):
  """ expects n = a decimal as a string.  e.g. 37.1, 37., 22.00.  NOT M23.4, etc.
      returns 1) the string, if n of the form #.##, where # != 0
              2) an array [#.#, #.#0] if n of the form #.# or #.#0
              3) an array [#, #., #.0, #.00] if n is an integer """
  num = float(n)
  if (num == math.trunc(num)):
    # e.g. 35, 35., 35.0, or 35.00
    result = []
    integer = str(math.trunc(num))
    result.append(integer)
    result.append(integer + ".")
    result.append(integer + ".0")
    result.append(integer + ".00")
    return result
  elif (num*10 == math.trunc(num*10)):
    # e.g. 31.1 or 31.10
    result = []
    integer = str(math.trunc(num*10))
    result.append(integer[:-1] + "." + integer[-1])
    result.append(integer[:-1] + "." + integer[-1] + "0")
    return result
  else:
    return [str(num)]

# push codes from the file into codes[]
with (open(inputFileName, 'r')) as inFile:
  codes = [line.strip('\n') for line in inFile]

# parse the codes
for code in codes:
  if bool(re.search('[a-zA-Z]', code)):
    letter = code[0].upper()
    number = code[1:]
    for parsed in parseCode(number):
      parsedCodes.append(letter + parsed)
  else:
    for parsed in parseCode(code):
      parsedCodes.append(parsed)

# Generate the output string
parsedCodeList = sorted(set(parsedCodes))
for code in parsedCodeList:
  if i == 0:
    outCode += '('
  outCode += "'" + code + "'"
  if i == len(parsedCodeList)-1:
    outCode += ")"
  else:
    outCode += ", "
    i += 1

print('\n' + 'Nicely formatted code list:')
print(outCode)
# outCodeWrapped = textwrap.wrap(outCode, 80, break_long_words = False)
# print(outCodeWrapped)
