-- Z SQL Method
-- /article17/wiki_trail/sql_methods/lookup_wiki_comments
<params>id</params>
SELECT comment
FROM wiki_trail_comments
WHERE <dtml-sqltest name="id" column="id" type=int>