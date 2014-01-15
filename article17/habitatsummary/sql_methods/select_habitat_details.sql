-- Z SQL Method
-- /article17/habitatsummary/sql_methods/select_habitat_details
<params>habitatcode
region</params>
SELECT *
FROM
  etc_data_habitattype_regions
WHERE <dtml-sqltest habitatcode type=string>
<dtml-if region>
AND <dtml-sqltest region type=string>
</dtml-if>
ORDER BY region, habitattype_type_asses, eu_country_code