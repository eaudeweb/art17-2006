-- Z SQL Method
-- /article17/wiki_trail/sql_methods/inactivate_wiki_changes
<params>id</params>
UPDATE 
  `wiki_trail_changes`
SET `active` = 0
WHERE <dtml-sqltest name="id" column="wiki_id" type="int">