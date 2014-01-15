-- Z SQL Method
-- /article17/habitatsummary/sql_methods/select_comment_by_id
<params>id</params>
SELECT comment
FROM habitat_comments
WHERE <dtml-sqltest name="id" column="id" type=string>