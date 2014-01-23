-- Z SQL Method
-- /article17/habitatsreport/sql_methods/lookup_country_name
<params>code</params>
SELECT 
  `name`
FROM 
  `dic_country_codes`
WHERE <dtml-sqltest name="code" column="codeEU" type=string>