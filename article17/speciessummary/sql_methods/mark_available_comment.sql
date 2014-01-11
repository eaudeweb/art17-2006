-- Z SQL Method
-- /article17/speciessummary/sql_methods/mark_available_comment
<params>id</params>
UPDATE 
  `comments`
SET `deleted` = NULL
WHERE <dtml-sqltest name="id" column="id" type=string>