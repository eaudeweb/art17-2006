-- Z SQL Method
-- /article17/speciesprogress/sql_methods/select_countries
<params></params>
call proc_species_countries(@o)
<dtml-var sql_delimiter>
select @o as thecount