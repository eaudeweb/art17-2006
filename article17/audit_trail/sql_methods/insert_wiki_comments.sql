-- Z SQL Method
-- /article17/wiki_trail/sql_methods/insert_wiki_comments
<params>wiki_id
comment
author</params>
INSERT INTO 
  `wiki_trail_comments`
(
  `wiki_id`,
  `comment`,
  `author`
) 
VALUE (
  <dtml-sqlvar wiki_id type=int>,
  <dtml-sqlvar comment type=string>,
  <dtml-sqlvar author type=string>
)

<dtml-var sql_delimiter>

SELECT LAST_INSERT_ID() AS newid