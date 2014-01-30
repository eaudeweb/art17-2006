-- Z SQL Method
-- /article17/wiki_trail/sql_methods/delete_wiki_comments
<params>id</params>
UPDATE 
  `wiki_trail_comments`
SET `deleted` = 1
WHERE <dtml-sqltest name="id" column="id" type=string>