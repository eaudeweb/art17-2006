-- Z SQL Method
-- /article17/wiki/sql_methods/select_wiki_changes
<params>id</params>
SELECT 
  `id`,
  `wiki_id`,
  `editor`,
  `changed`,
  `active`
FROM 
  `wiki_changes`
WHERE <dtml-sqltest name="id" column="wiki_id" type="int">
ORDER BY changed DESC