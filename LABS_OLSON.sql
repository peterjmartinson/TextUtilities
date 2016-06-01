drop table OLSON_SR1028444_L;
create table OLSON_SR1028444_L nologging as
select
  I.*
from
  OLSON_SR1028444_PTS P
  inner join ODS.ENCOUNTER E
    on P.VISIT_NUMBER_NUM = E.VISIT_NUMBER_NUM
    and E.SOURCE_CODE IN ('SCM','EPIC')
  inner join ODS.ORDERS O
    on E.PK_ENCOUNTER_ID = O.FK_ENCOUNTER_ID
    and O.SOURCE_CODE IN ('SCM','EPIC')
  inner join ODS.ORDER_RESULT R
    on O.PK_ORDER_ID = R.FK_ORDER_ID
    and R.SOURCE_CODE IN ('SCM','EPIC')
  inner join ODS.R_RESULT_ITEM I
    on I.PK_RESULT_ITEM_ID = R.FK_RESULT_ITEM_ID
    and I.SOURCE_CODE IN ('SCM','EPIC')
where E.ORDER_DATE >= to_date('01/01/2006','MM/DD/YYYY')
  and E.ORDER_DATE <= to_date('01/01/2010','MM/DD/YYYY')
;
