-- Z SQL Method
-- /article17/speciessummary/sql_methods/update_decision
<params>decision
user_decision
last_update_decision
region
assesment_speciesname
user</params>
UPDATE 
  `species_manual_assessment`
SET `decision` = <dtml-sqlvar decision type=string>,
  `user_decision` = <dtml-sqlvar user_decision type=string>,
  `last_update_decision` = <dtml-sqlvar last_update_decision type=string>
WHERE <dtml-sqltest region type=string>
AND <dtml-sqltest assesment_speciesname type=string>
AND <dtml-sqltest user type=string>