-- Z SQL Method
-- /article17/wiki_trail/sql_methods/update_wiki_comments
<params>id
comment</params>
UPDATE 
  `wiki_trail_comments`
SET `comment` = <dtml-sqlvar comment type=string>
WHERE <dtml-sqltest name="id" column="id" type="int">