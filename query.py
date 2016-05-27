# -*- coding: utf-8 -*-
"""
Build a blank QUERY_<NAME>.sql file
"""
import csv

out = []

out.append('ALTER SESSION SET STAR_TRANSFORMATION_ENABLED=FALSE;')
out.append('/*')
out.append(' * Reqester:    ')
out.append(' * Title:       ')
out.append(' * Ticket:      ')
out.append(' *')
out.append(' * Author:      ')
out.append(' * Open Date:   ')
out.append(' * Close Date:  ')
out.append(' *')
out.append(' * Description: ')
out.append('*/')
out.append('')
out.append('/*================================= NOTES ======================================')
out.append('')
out.append('')
out.append('/*=============================== END NOTES ==================================*/')
out.append('')
out.append('/*_____________________________ Build the Query ______________________________*/')
out.append('')

requester   = input("Requester's name (e.g. First Last): ")
user = requester.split(" ")
title       = input("Title of report: ")
ticket      = input("Ticket number (e.g. SR1234567): ")
author      = input("Author name (e.g. First Last): ")
description = input("Description (don't include carriage returns): ")

out[2]  = out[2]  + user[0] + ' ' + user[1]
out[3]  = out[3]  + title
out[4]  = out[4]  + ticket
out[6]  = out[6]  + author
out[10] = out[10] + description

outFileName = 'QUERY_' + user[1].upper() + '.sql'

with(open(outFileName, 'w')) as outFile:

  for element in out:
    outFile.write(element + '\n')

# fin
