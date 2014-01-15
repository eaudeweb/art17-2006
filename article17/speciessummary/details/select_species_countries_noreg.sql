-- Z SQL Method
-- /article17/speciessummary/details/select_species_countries_noreg
<params>assesment_speciesname</params>
SELECT 
  etc_data_species_regions.eu_country_code,
  etc_data_species_regions.code,
  etc_data_species_regions.conclusion_assessment
FROM
  etc_data_species_regions
WHERE <dtml-sqltest assesment_speciesname type=string>