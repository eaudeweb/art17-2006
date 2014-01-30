-- Z SQL Method
-- /article17/wiki_trail/sql_methods/delete_user_wiki_comments_read
<params>comment_id
reader_id</params>
DELETE FROM 
  `wiki_trail_comments_read` 
WHERE <dtml-sqltest comment_id type=int>
AND <dtml-sqltest reader_id type=string>