-- Z SQL Method
-- /article17/habitatsreport/sql_methods/lookup_qa_errors
<params>habitatcode
region
eu_country_code
</params>
SELECT FlagField, FlagText, suspect_value
FROM etc_qa_errors_habitattype_manual_checked
WHERE <dtml-sqltest habitatcode type=string>
AND <dtml-sqltest region type=string>
AND <dtml-sqltest eu_country_code type=string>