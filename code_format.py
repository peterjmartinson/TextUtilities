import math
import re

nums = ['34.00','M34.1','34.2','34.81','34.82','34.83','34.89','34.9','710.1','710.0']
# check to see if there are [a-zA-Z] in the code
#   if so, need to do something different!
# check to see if there's a "."
#   if no ".", then append ##, ##., ##.0, ##.00 to the output array
# check to see if it's an integer (e.g. 34.0)
# -> convert to float, check if (num == math.trunc(num))
#   if yes, then append ##, ##., ##.0, ##.00 to the output array
# count number of decimal places
#   if 0, append ##, ##., ##.0, ##.00 to the output array
#   if 1, append ##.# and ##.#0 to output array
#   if 2, see if last digit is 0
#     if no, append the number as-is
#     if yes, append ##.# and ##.##
# print the whole array as comma-separated, quoted values


for code in nums:
  if bool(re.search('[a-zA-Z]', code)):
    print(code + " there's a letter")
  else:
    print("string: " + code)
    num = float(code)
    print("float:  " + str(num))
    if (num == math.trunc(num)):
      fourIntegers = []
      justInteger = str(math.trunc(num))
      fourIntegers.append(justInteger)
      fourIntegers.append(justInteger + ".")
      fourIntegers.append(justInteger + ".0")
      fourIntegers.append(justInteger + ".00")
      for element in fourIntegers:
        print(element)
