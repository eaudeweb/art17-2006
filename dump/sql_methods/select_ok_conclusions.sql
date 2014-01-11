-- Z SQL Method
-- /article17/speciessummary/sql_methods/select_ok_conclusions
<params>assesment_speciesname
bioregion</params>
SELECT decision
FROM `species_manual_assessment`
WHERE <dtml-sqltest assesment_speciesname type=string>
AND <dtml-sqltest name="bioregion" column="region" type=string>
AND decision = 'OK'