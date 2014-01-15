-- Z SQL Method
-- /article17/habitatsummary/sql_methods/select_comments_number
<params>region
habitat
user
ms</params>
SELECT id
FROM habitat_comments
WHERE <dtml-sqltest region type=string>
AND <dtml-sqltest habitat type=string>
AND <dtml-sqltest user type=string>
AND <dtml-sqltest name="ms" column="MS" type=string>