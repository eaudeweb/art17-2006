-- Z SQL Method
-- /article17/wiki/sql_methods/select_wiki_comments_read
<params>reader_id</params>
SELECT 
  `comment_id`
FROM 
  `wiki_comments_read`
WHERE <dtml-sqltest reader_id type=string>