-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_country_assessment
<params>assesment_speciesname
region
eu_country_code</params>
SELECT * 
FROM `etc_data_species_regions`
WHERE <dtml-sqltest assesment_speciesname type=string>
AND <dtml-sqltest region type=string>
AND <dtml-sqltest eu_country_code type=string>