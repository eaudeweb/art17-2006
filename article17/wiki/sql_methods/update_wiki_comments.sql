-- Z SQL Method
-- /article17/wiki/sql_methods/update_wiki_comments
<params>id
comment</params>
UPDATE 
  `wiki_comments`
SET `comment` = <dtml-sqlvar comment type=string>
WHERE <dtml-sqltest name="id" column="id" type="int">