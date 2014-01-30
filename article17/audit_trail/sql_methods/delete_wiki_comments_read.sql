-- Z SQL Method
-- /article17/wiki_trail/sql_methods/delete_wiki_comments_read
<params>id
user</params>
DELETE FROM 
  `wiki_trail_comments_read` 
WHERE 
<dtml-sqltest name="id" column="comment_id" type=int>
AND reader_id <> <dtml-sqlvar user type=string> 