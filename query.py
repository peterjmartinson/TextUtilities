# -*- coding: utf-8 -*-
"""
Build a blank QUERY_<NAME>.sql file
"""
import textwrap
import datetime
out = []

out.append('alter session set STAR_TRANSFORMATION_ENABLED=FALSE;')
out.append('/*')
out.append(' * Requester:    ')
out.append(' * Title:       ')
out.append(' * Ticket:      ')
out.append(' *')
out.append(' * Author:      ')
out.append(' * Open Date:   ')
out.append(' * Close Date:  ')
out.append(' *')
out.append(' * Description: ')
out.append(' *              ')
out.append('*/')
out.append('')
out.append('/*================================= NOTES ======================================')
out.append('')
out.append('')
out.append('/*=============================== END NOTES ==================================*/')
out.append('')
out.append('/*_____________________________ Build the Query ______________________________*/')
out.append('')
out.append('')
out.append('')
out.append('/*______________________________ Report Tables _______________________________*/')
out.append('')

requester   = input("Requester's name (e.g. First Last): ")
user = requester.split(" ")
title       = input("Title of report: ")
ticket      = input("Ticket number (e.g. SR1234567): ")
author      = input("Author name (e.g. First Last): ")
description = input("Description (don't include carriage returns): ")
date        = datetime.datetime.now().strftime("%B %d, %Y").lstrip("0").replace(" 0", " ")

out[2]  = out[2]  + user[0] + ' ' + user[1]
out[3]  = out[3]  + title
out[4]  = out[4]  + ticket.upper()
out[6]  = out[6]  + author
out[7]  = out[7]  + date

descriptionLines = textwrap.wrap(description, (80-17), break_long_words=False)

outFileName = 'QUERY_' + user[1].upper() + '.sql'

with(open(outFileName, 'w')) as outFile:
  for element in out[0:10]:
    outFile.write(element + '\n')
  outFile.write(out[10] + descriptionLines[0] + '\n')
  for element in descriptionLines[1:]:
    outFile.write(out[11] + element + '\n')
  for element in out[12:]:
    outFile.write(element + '\n')

# fin
