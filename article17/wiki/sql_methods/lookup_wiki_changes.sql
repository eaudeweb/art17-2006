-- Z SQL Method
-- /article17/wiki/sql_methods/lookup_wiki_changes
<params>id</params>
SELECT 
  `body`
FROM 
  `wiki_changes`
WHERE <dtml-sqltest name="id" column="id" type=int>