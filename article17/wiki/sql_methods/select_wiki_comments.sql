-- Z SQL Method
-- /article17/wiki/sql_methods/select_wiki_comments
<params>id</params>
SELECT 
  `id`,
  `wiki_id`,
  `comment`,
  `author`,
  `deleted`,
  `posted`
FROM 
  `wiki_comments`
WHERE <dtml-sqltest name="id" column="wiki_id" type="int">
ORDER BY deleted, posted