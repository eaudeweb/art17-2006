-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_comment_by_id
<params>id</params>
SELECT comment
FROM comments
WHERE <dtml-sqltest name="id" column="id" type=string>