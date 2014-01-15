-- Z SQL Method
-- /article17/habitatsummary/sql_methods/get_coverage_conclusion_value
<params>habitatcode
region
assessment_method
</params>
SELECT 
  percentage_coverage_surface_area
FROM
  etc_data_habitattype_automatic_assessment
WHERE <dtml-sqltest habitatcode type=string>
AND <dtml-sqltest region type=string>
AND <dtml-sqltest assessment_method type=string>