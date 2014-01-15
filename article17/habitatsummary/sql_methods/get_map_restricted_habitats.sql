-- Z SQL Method
-- /article17/habitatsummary/sql_methods/get_map_restricted_habitats
<params>habitatcode</params>
SELECT `eu_country_code`, `habitatcode`
FROM `restricted_habitats`
WHERE <dtml-sqltest habitatcode type=string>