-- Z SQL Method
-- /article17/wiki_trail/sql_methods/undelete_wiki_comments
<params>id</params>
UPDATE 
  `wiki_trail_comments`
SET `deleted` = NULL
WHERE <dtml-sqltest name="id" column="id" type=string>