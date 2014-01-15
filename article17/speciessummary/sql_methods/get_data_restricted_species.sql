-- Z SQL Method
-- /article17/speciessummary/sql_methods/get_data_restricted_species
<params>assesment_speciesname</params>
SELECT `eu_country_code`
FROM `restricted_species`
WHERE <dtml-sqltest assesment_speciesname type=string>
AND show_data = 0