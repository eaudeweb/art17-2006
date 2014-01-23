-- Z SQL Method
-- /article17/speciesreport/sql_methods/lookup_country_bioregion
<params>country</params>
SELECT DISTINCT region
FROM 
  `etc_data_species_regions`
<dtml-if country>
WHERE <dtml-sqltest name="country" column="eu_country_code" type=string>
</dtml-if>
ORDER BY region