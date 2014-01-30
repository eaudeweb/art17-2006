-- Z SQL Method
-- /article17/wiki/sql_methods/activate_wiki_changes
<params>id</params>
UPDATE 
  `wiki_changes`
SET `active` = 1
WHERE <dtml-sqltest name="id" column="id" type="int">