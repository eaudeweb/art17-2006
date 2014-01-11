-- Z SQL Method
-- /article17/speciessummary/sql_methods/get_map_restricted_species
<params>assesment_speciesname</params>
SELECT `eu_country_code`, `assesment_speciesname`
FROM `restricted_species`
WHERE <dtml-sqltest assesment_speciesname type=string>