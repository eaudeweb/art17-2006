-- Z SQL Method
-- /article17/habitatsummary/sql_methods/insert_comment
<params>region
habitat
user
ms
comment
author
post_date</params>
INSERT INTO 
  `habitat_comments`
(
  `region`,
  `habitat`,
  `user`,
  `MS`,
  `comment`,
  `author`,
  `post_date`
) 
VALUE (
  <dtml-sqlvar region type=string>,
  <dtml-sqlvar habitat type=string>,
  <dtml-sqlvar user type=string>,
  <dtml-sqlvar ms type=string>,
  <dtml-sqlvar comment type=string>,
  <dtml-sqlvar author type=string>,
  <dtml-sqlvar post_date type=string>
)
<dtml-var sql_delimiter>
SELECT LAST_INSERT_ID() AS newid