-- Z SQL Method
-- /article17/speciessummary/sql_methods/list_group_species
<params>group</params>
SELECT DISTINCT `assesment_speciesname`
FROM etc_data_species_regions
WHERE <dtml-sqltest name="group" column="etc_data_species_regions.group" type=string> 
ORDER BY assesment_speciesname