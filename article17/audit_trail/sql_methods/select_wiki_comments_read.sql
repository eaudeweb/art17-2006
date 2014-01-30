-- Z SQL Method
-- /article17/wiki_trail/sql_methods/select_wiki_comments_read
<params>reader_id</params>
SELECT 
  `comment_id`
FROM 
  `wiki_trail_comments_read`
WHERE <dtml-sqltest reader_id type=string>