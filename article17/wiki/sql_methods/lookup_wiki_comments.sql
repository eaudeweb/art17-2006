-- Z SQL Method
-- /article17/wiki/sql_methods/lookup_wiki_comments
<params>id</params>
SELECT comment
FROM wiki_comments
WHERE <dtml-sqltest name="id" column="id" type=int>