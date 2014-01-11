-- Z SQL Method
-- /article17/speciessummary/sql_methods/set_comments_unread
<params>id_comment
reader_user_id</params>
DELETE FROM 
  `comments_read` 
WHERE <dtml-sqltest id_comment type=string>
AND <dtml-sqltest reader_user_id type=string>