-- Z SQL Method
-- /article17/wiki/sql_methods/count_wiki_comments
<params>wiki_id</params>
SELECT COUNT(`id`) as no_id
FROM 
  `wiki_comments`
WHERE wiki_id 