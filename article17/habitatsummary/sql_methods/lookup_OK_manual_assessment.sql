-- Z SQL Method
-- /article17/habitatsummary/sql_methods/lookup_OK_manual_assessment
<params>habitatcode
region</params>
SELECT *
FROM `habitattypes_manual_assessment`
WHERE <dtml-sqltest habitatcode type=string>
AND <dtml-sqltest region type=string>
AND decision = 'OK'