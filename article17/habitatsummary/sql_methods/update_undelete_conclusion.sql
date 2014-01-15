-- Z SQL Method
-- /article17/habitatsummary/sql_methods/update_undelete_conclusion
<params>region
habitatcode
user
ms
last_update</params>
UPDATE 
  `habitattypes_manual_assessment`
SET `last_update` = <dtml-sqlvar last_update type=string>,
  `deleted_record` = 0
WHERE <dtml-sqltest region type=string>
AND <dtml-sqltest habitatcode type=string>
AND <dtml-sqltest user type=string>
AND <dtml-sqltest name="ms" column="MS" type=string>