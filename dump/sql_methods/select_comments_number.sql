-- Z SQL Method
-- /article17/speciessummary/sql_methods/select_comments_number
<params>region
assesment_speciesname
user
ms</params>
SELECT id
FROM comments
WHERE <dtml-sqltest region type=string>
AND <dtml-sqltest assesment_speciesname type=string>
AND <dtml-sqltest name="user" column="comments.user" type=string>
AND <dtml-sqltest name="ms" column="comments.MS" type=string>