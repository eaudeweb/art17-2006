-- Z SQL Method
-- /article17/speciessummary/sql_methods/list_groups
<params></params>
SELECT DISTINCT etc_data_species_regions.group as upper_group 
FROM etc_data_species_regions 
ORDER BY etc_data_species_regions.group