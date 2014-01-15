-- Z SQL Method
-- /article17/habitatsummary/sql_methods/lookup_method_conclusions
<params>habitatcode
region
</params>
SELECT 
  assessment_method,
  conclusion_range,
  conclusion_coverage,
  conclusion_structure,
  conclusion_future,
  conclusion_assessment
FROM
  etc_data_habitattype_automatic_assessment
WHERE <dtml-sqltest habitatcode type=string>
AND <dtml-sqltest region type=string>