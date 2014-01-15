-- Z SQL Method
-- /article17/speciessummary/sql_methods/mark_delete_comment
<params>id</params>
UPDATE 
  `comments`
SET `deleted` = 1
WHERE <dtml-sqltest name="id" column="id" type=string>