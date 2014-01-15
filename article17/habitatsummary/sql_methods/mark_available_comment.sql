-- Z SQL Method
-- /article17/habitatsummary/sql_methods/mark_available_comment
<params>id</params>
UPDATE 
  `habitat_comments`
SET `deleted` = NULL
WHERE <dtml-sqltest name="id" column="id" type=string>