-- Z SQL Method
-- /article17/speciessummary/sql_methods/update_delete_conclusion
<params>region
assesment_speciesname
user
ms
last_update</params>
UPDATE 
  `species_manual_assessment`
SET `last_update` = <dtml-sqlvar last_update type=string>,
  `deleted_record` = 1
WHERE <dtml-sqltest region type=string>
AND <dtml-sqltest assesment_speciesname type=string>
AND <dtml-sqltest user type=string>
AND <dtml-sqltest name="ms" column="MS" type=string>