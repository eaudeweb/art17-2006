-- Z SQL Method
-- /article17/habitatsummary/sql_methods/lookup_country_assessment
<params>habitatcode
region
eu_country_code</params>
SELECT * 
FROM `etc_data_habitattype_regions`
WHERE <dtml-sqltest habitatcode type=string>
AND <dtml-sqltest region type=string>
AND <dtml-sqltest eu_country_code type=string>