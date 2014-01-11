-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_method_conclusions
<params>assesment_speciesname
region</params>
SELECT 
  assessment_method,
  conclusion_range,
  conclusion_population,
  conclusion_habitat,
  conclusion_future,
  conclusion_assessment
FROM
  etc_data_species_automatic_assessment
WHERE <dtml-sqltest assesment_speciesname type=string>
AND <dtml-sqltest region type=string>