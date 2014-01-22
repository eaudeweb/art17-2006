-- Z SQL Method
-- /article17/habitatsprogress/sql_methods/select_countries
<params></params>
call proc_habitat_countries(@o)
<dtml-var sql_delimiter>
select @o as thecount