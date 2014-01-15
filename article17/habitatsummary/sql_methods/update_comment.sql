-- Z SQL Method
-- /article17/habitatsummary/sql_methods/update_comment
<params>id
comment
post_date</params>
UPDATE
  `habitat_comments`
SET `comment` = <dtml-sqlvar comment type=string>, 
    `post_date` = <dtml-sqlvar post_date type=string>
WHERE <dtml-sqltest name="id" column="id" type=string>