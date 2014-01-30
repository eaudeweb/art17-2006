-- Z SQL Method
-- /article17/wiki/sql_methods/delete_wiki_comments
<params>id</params>
UPDATE 
  `wiki_comments`
SET `deleted` = 1
WHERE <dtml-sqltest name="id" column="id" type=string>