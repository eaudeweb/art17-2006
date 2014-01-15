-- Z SQL Method
-- /article17/speciessummary/sql_methods/select_read_comments
<params>reader_user_id</params>
SELECT 
  `id_comment`
FROM 
  `comments_read`
WHERE <dtml-sqltest reader_user_id type=string>