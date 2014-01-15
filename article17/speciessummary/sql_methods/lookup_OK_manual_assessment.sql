-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_OK_manual_assessment
<params>assesment_speciesname
region</params>
SELECT *
FROM `species_manual_assessment`
WHERE <dtml-sqltest assesment_speciesname type=string>
AND <dtml-sqltest region type=string>
AND decision = 'OK'