-- Z SQL Method
-- /article17/speciessummary/sql_methods/get_future_conclusion_value
<params>assesment_speciesname
region
assessment_method
</params>
SELECT 
  percentage_future
FROM
  etc_data_species_automatic_assessment
WHERE <dtml-sqltest assesment_speciesname type=string>
AND <dtml-sqltest region type=string>
AND <dtml-sqltest assessment_method type=string>