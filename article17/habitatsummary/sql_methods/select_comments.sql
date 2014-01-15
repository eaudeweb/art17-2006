-- Z SQL Method
-- /article17/habitatsummary/sql_methods/select_comments
<params>region
habitat
user
ms</params>
SELECT id, comment, author, post_date, habitat_comments.deleted
FROM habitat_comments
WHERE <dtml-sqltest region type=string>
AND <dtml-sqltest habitat type=string>
AND <dtml-sqltest name="user" column="habitat_comments.user" type=string>
AND <dtml-sqltest name="ms" column="habitat_comments.MS" type=string>
ORDER BY habitat_comments.deleted, post_date