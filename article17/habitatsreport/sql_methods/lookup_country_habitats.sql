-- Z SQL Method
-- /article17/habitatsreport/sql_methods/lookup_country_habitats
<params>group
country
region</params>
SELECT * 
FROM 
  `etc_data_habitattype_regions`
WHERE <dtml-sqltest name="group" column="etc_data_habitattype_regions.group" type=string>
<dtml-if country>
	AND <dtml-sqltest name="country" column="etc_data_habitattype_regions.eu_country_code" type=string>
</dtml-if>
<dtml-if region>
	AND <dtml-sqltest name="region" column="etc_data_habitattype_regions.region" type=string>
</dtml-if>
ORDER BY habitattype_type_asses, habitatcode, region