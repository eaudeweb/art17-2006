-- Z SQL Method
-- /article17/habitatsprogress/sql_methods/select_trail_comments
<params>user_id</params>
call proc_habitat_trail_comments('<dtml-var user_id>', @o)
<dtml-var sql_delimiter>
select @o as thecount