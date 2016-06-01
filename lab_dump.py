# -*- coding: utf-8 -*-
"""
Build a blank QUERY_<NAME>.sql file
"""
import datetime

print("Remember: garbage in, garbage out.")
requester = input("Requester's last name: ")
ticket    = input("Ticket number: ")
startDate = input("Start Date (MM/DD/YYYY): ")
endDate   = input("End Date (MM/DD/YYYY): ")
visitFlag = input("Labs by patient (1) or by visit (2)? ")

# convert the dates to date objects
dateBegin = datetime.datetime.strptime(startDate,"%m/%d/%Y")
dateEnd = datetime.datetime.strptime(endDate,"%m/%d/%Y")

"""if (visitFlag != 1) or (visitFlag != 2):
  sys.exit()
"""
if ( dateBegin < datetime.datetime.strptime("05/18/2008", "%m/%d/%Y")
    and dateEnd >= datetime.datetime.strptime("05/18/2008", "%m/%d/%Y") ):
  sources = "('SCM','CERNER','EPIC')"
if ( dateBegin < datetime.datetime.strptime("05/18/2008", "%m/%d/%Y")
    and dateEnd < datetime.datetime.strptime("05/18/2008", "%m/%d/%Y") ):
  sources = "('SCM','EPIC')"
if ( dateBegin >= datetime.datetime.strptime("05/18/2008", "%m/%d/%Y")
    and dateEnd >= datetime.datetime.strptime("05/18/2008", "%m/%d/%Y") ):
  sources = "('CERNER','EPIC')"

out = []
out.append('drop table ' + requester.upper() + '_' + ticket.upper() + '_' + 'L;')
out.append('create table ' + requester.upper() + '_' + ticket.upper() + '_' + 'L nologging as')
out.append('select')
out.append('  I.*')
out.append('from')
out.append('  ' + requester.upper() + '_' + ticket.upper() + '_PTS P')
print("visitFlag = " + visitFlag)
if visitFlag == 1 : #goes straight to the else
    out.append('  inner join ODS.PATIENT OP')
    out.append('    on P.MDM_PATIENT_ID = OP.MDM_PATIENT_ID')
    out.append('    and OP.SOURCE_CODE IN ' + sources)
    out.append('  inner join ODS.ENCOUNTER E')
    out.append('    on OP.PK_PATIENT_ID = E.FK_PATIENT_ID')
    out.append('    and E.SOURCE_CODE IN ' + sources)
else :
    out.append('  inner join ODS.ENCOUNTER E')
    out.append('    on P.VISIT_NUMBER_NUM = E.VISIT_NUMBER_NUM')
    out.append('    and E.SOURCE_CODE IN ' + sources)

out.append('  inner join ODS.ORDERS O')
out.append('    on E.PK_ENCOUNTER_ID = O.FK_ENCOUNTER_ID')
out.append('    and O.SOURCE_CODE IN ' + sources)
out.append('  inner join ODS.ORDER_RESULT R')
out.append('    on O.PK_ORDER_ID = R.FK_ORDER_ID')
out.append('    and R.SOURCE_CODE IN ' + sources)
out.append('  inner join ODS.R_RESULT_ITEM I')
out.append('    on I.PK_RESULT_ITEM_ID = R.FK_RESULT_ITEM_ID')
out.append('    and I.SOURCE_CODE IN ' + sources)
out.append("where E.ORDER_DATE >= to_date('" + dateBegin.strftime("%m/%d/%Y") + "','MM/DD/YYYY')")
out.append("  and E.ORDER_DATE <= to_date('" + dateEnd.strftime("%m/%d/%Y")   + "','MM/DD/YYYY')")
out.append(';')



outFileName = 'LABS_' + requester.upper() + '.sql'

with(open(outFileName, 'w')) as outFile:
  for element in out:
    outFile.write(element + '\n')

