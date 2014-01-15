-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_ms_countries
<params>assesment_speciesname
bioregion</params>
SELECT 
  `eu_country_code`
FROM 
  `etc_data_species_regions`
WHERE <dtml-sqltest assesment_speciesname type=string>
AND <dtml-sqltest name="bioregion" column="region" type=string>
ORDER BY species_type_asses, eu_country_code