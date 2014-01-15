-- Z SQL Method
-- /article17/habitatsummary/sql_methods/mark_delete_comment
<params>id</params>
UPDATE 
  `habitat_comments`
SET `deleted` = 1
WHERE <dtml-sqltest name="id" column="id" type=string>