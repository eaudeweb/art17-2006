-- Z SQL Method
-- /article17/wiki_trail/sql_methods/count_wiki_comments
<params>wiki_id</params>
SELECT COUNT(`id`) as no_id
FROM 
  `wiki_trail_comments`
WHERE wiki_id = 1