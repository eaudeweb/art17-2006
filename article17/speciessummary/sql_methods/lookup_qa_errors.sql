-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_qa_errors
<params>assesment_speciesname
region
eu_country_code
</params>
SELECT FlagField, FlagText, suspect_value
FROM etc_qa_errors_species_manual_checked
WHERE <dtml-sqltest assesment_speciesname type=string>
AND <dtml-sqltest region type=string>
AND <dtml-sqltest eu_country_code type=string>