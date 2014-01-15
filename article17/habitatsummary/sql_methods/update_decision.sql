-- Z SQL Method
-- /article17/habitatsummary/sql_methods/update_decision
<params>decision
user_decision
last_update_decision
region
habitatcode
user</params>
UPDATE 
  `habitattypes_manual_assessment`
SET `decision` = <dtml-sqlvar decision type=string>,
  `user_decision` = <dtml-sqlvar user_decision type=string>,
  `last_update_decision` = <dtml-sqlvar last_update_decision type=string>
WHERE <dtml-sqltest region type=string>
AND <dtml-sqltest habitatcode type=string>
AND <dtml-sqltest user type=string>