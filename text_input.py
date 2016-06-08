inputFileName = 'temp.txt'
codes = []
with (open(inputFileName, 'r')) as inFile:
  codes = [line.strip('\n') for line in inFile]
print(codes)
