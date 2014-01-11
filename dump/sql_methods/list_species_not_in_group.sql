-- Z SQL Method
-- /article17/speciessummary/sql_methods/list_species_not_in_group
<params></params>
SELECT DISTINCT speciesname
FROM etc_data_species_regions
WHERE etc_data_species_regions.group IS NULL AND etc_data_species_regions.valid_speciesname IS NULL
ORDER BY speciesname
