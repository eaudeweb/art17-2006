-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_comments
<params>region
assesment_speciesname
user
ms</params>
SELECT id, comment, author, post_date, comments.deleted
FROM comments
WHERE <dtml-sqltest region type=string>
AND <dtml-sqltest assesment_speciesname type=string>
AND <dtml-sqltest name="user" column="comments.user" type=string>
AND <dtml-sqltest name="ms" column="comments.MS" type=string>
ORDER BY comments.deleted, post_date