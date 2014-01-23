-- Z SQL Method
-- /article17/speciesreport/sql_methods/lookup_country_species
<params>group
country
region</params>
SELECT * 
FROM 
  `etc_data_species_regions`
WHERE <dtml-sqltest name="group" column="etc_data_species_regions.group" type=string>
<dtml-if country>
	AND <dtml-sqltest name="country" column="etc_data_species_regions.eu_country_code" type=string>
</dtml-if>
<dtml-if region>
	AND <dtml-sqltest name="region" column="region" type=string>
</dtml-if>
ORDER BY species_type_asses, assesment_speciesname, region