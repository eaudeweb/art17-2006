-- Z SQL Method
-- /article17/habitatsummary/sql_methods/insert_comments_read
<params>id_comment
reader_user_id</params>
INSERT INTO 
  `habitat_comments_read`
(
  `id_comment`,
  `reader_user_id`
) 
VALUE (
  <dtml-sqlvar id_comment type=string>,
  <dtml-sqlvar reader_user_id type=string>
)