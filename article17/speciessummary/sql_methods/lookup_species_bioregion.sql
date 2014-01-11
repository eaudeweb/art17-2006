-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_species_bioregion
<params>assesment_speciesname</params>
SELECT DISTINCT region
FROM etc_data_species_regions
WHERE <dtml-sqltest assesment_speciesname type=string>
ORDER BY region