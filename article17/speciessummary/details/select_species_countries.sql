-- Z SQL Method
-- /article17/speciessummary/details/select_species_countries
<params>region
assesment_speciesname</params>
SELECT 
  etc_data_species_regions.eu_country_code,
  etc_data_species_regions.code,
  etc_data_species_regions.conclusion_assessment,
  etc_data_species_regions.region
FROM
  etc_data_species_regions
WHERE 
<dtml-sqltest region type="string" multiple="multiple">
AND 
<dtml-sqltest assesment_speciesname type=string>