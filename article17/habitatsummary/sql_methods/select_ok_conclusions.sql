-- Z SQL Method
-- /article17/habitatsummary/sql_methods/select_ok_conclusions
<params>habitatcode
bioregion</params>
SELECT decision
FROM `habitattypes_manual_assessment`
WHERE <dtml-sqltest habitatcode type=string>
AND <dtml-sqltest name="bioregion" column="region" type=string>
AND decision = 'OK'