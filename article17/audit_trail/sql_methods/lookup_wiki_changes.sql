-- Z SQL Method
-- /article17/wiki_trail/sql_methods/lookup_wiki_changes
<params>id</params>
SELECT 
  `body`
FROM 
  `wiki_trail_changes`
WHERE <dtml-sqltest name="id" column="id" type=int>