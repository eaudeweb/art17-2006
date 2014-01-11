-- Z SQL Method
-- /article17/speciessummary/sql_methods/delete_comments_read
<params>id
user</params>
DELETE FROM 
  `comments_read` 
WHERE 
<dtml-sqltest name="id" column="id_comment" type=string>
AND reader_user_id <> <dtml-sqlvar user type=string> 