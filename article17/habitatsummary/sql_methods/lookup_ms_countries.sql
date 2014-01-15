-- Z SQL Method
-- /article17/habitatsummary/sql_methods/lookup_ms_countries
<params>habitatcode
bioregion</params>
SELECT 
  `eu_country_code`
FROM 
  `etc_data_habitattype_regions`
WHERE <dtml-sqltest habitatcode type=string>
AND <dtml-sqltest name="bioregion" column="region" type=string>
ORDER BY habitattype_type_asses, eu_country_code