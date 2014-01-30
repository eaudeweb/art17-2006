-- Z SQL Method
-- /article17/wiki_trail/sql_methods/select_wiki_changes
<params>id</params>
SELECT 
  `id`,
  `wiki_id`,
  `editor`,
  `changed`,
  `active`
FROM 
  `wiki_trail_changes`
WHERE <dtml-sqltest name="id" column="wiki_id" type="int">
ORDER BY changed DESC