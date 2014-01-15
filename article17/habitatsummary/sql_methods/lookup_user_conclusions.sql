-- Z SQL Method
-- /article17/habitatsummary/sql_methods/lookup_user_conclusions
<params>region
habitatcode
user</params>
SELECT
  `MS`, `user`
FROM 
  `habitattypes_manual_assessment`
WHERE
  <dtml-sqltest region type=string>
AND <dtml-sqltest habitatcode type=string>
AND <dtml-sqltest user type=string>