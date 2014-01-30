-- Z SQL Method
-- /article17/wiki_trail/sql_methods/insert_wiki_comments_read
<params>comment_id
reader_id</params>
INSERT INTO 
  `wiki_trail_comments_read`
(
  `comment_id`,
  `reader_id`
) 
VALUE (
  <dtml-sqlvar comment_id type=int>,
  <dtml-sqlvar reader_id type=string>
)