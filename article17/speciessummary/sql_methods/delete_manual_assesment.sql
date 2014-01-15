-- Z SQL Method
-- /article17/speciessummary/sql_methods/delete_manual_assesment
<params>region
assesment_speciesname</params>
DELETE FROM `species_manual_assessment`
WHERE `region` = <dtml-sqlvar region type=string>
AND `assesment_speciesname` = <dtml-sqlvar assesment_speciesname type=string>
