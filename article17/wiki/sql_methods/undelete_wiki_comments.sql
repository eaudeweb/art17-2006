-- Z SQL Method
-- /article17/wiki/sql_methods/undelete_wiki_comments
<params>id</params>
UPDATE 
  `wiki_comments`
SET `deleted` = NULL
WHERE <dtml-sqltest name="id" column="id" type=string>