-- Z SQL Method
-- /article17/habitatsummary/sql_methods/get_data_restricted_habitats
<params>habitatcode</params>
SELECT `eu_country_code` 
FROM `restricted_habitats`
WHERE <dtml-sqltest habitatcode type=string>
AND show_data = 0