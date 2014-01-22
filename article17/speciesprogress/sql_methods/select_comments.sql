-- Z SQL Method
-- /article17/speciesprogress/sql_methods/select_comments
<params>user_id</params>
call proc_species_comments('<dtml-var user_id>', @o)
<dtml-var sql_delimiter>
select @o as thecount