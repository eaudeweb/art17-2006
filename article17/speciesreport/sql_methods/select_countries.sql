-- Z SQL Method
-- /article17/speciesreport/sql_methods/select_countries
<params></params>
SELECT 
  `codeEU` as code,
  `name`
FROM 
  `dic_country_codes`
ORDER BY name