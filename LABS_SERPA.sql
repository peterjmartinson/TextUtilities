drop table SERPA_SR123456_L;
create table SERPA_SR123456_L nologging as
select
  I.*
from
  SERPA_SR123456_PTS P
  inner join ODS.ORDERS O
    on E.PK_ENCOUNTER_ID = O.FK_ENCOUNTER_ID
    and O.SOURCE_CODE IN ('SCM','EPIC')
  inner join ODS.ORDER_RESULT R
    on O.PK_ORDER_ID = R.FK_ORDER_ID
    and R.SOURCE_CODE IN ('SCM','EPIC')
  inner join ODS.R_RESULT_ITEM I
    on I.PK_RESULT_ITEM_ID = R.FK_RESULT_ITEM_ID
    and I.SOURCE_CODE IN ('SCM','EPIC')
where E.ORDER_DATE >= to_date('01/01/2011','MM/DD/YYYY')
  and E.ORDER_DATE <= to_date('01/01/2015','MM/DD/YYYY')
;
