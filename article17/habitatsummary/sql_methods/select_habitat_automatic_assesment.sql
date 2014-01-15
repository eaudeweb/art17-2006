-- Z SQL Method
-- /article17/habitatsummary/sql_methods/select_habitat_automatic_assesment
<params>habitatcode
region</params>
SELECT 
  `assessment_method`,
  `order`,
  `habitatcode`,
  `region`,
  `range_surface_area`,
  `percentage_range_surface_area`,
  `range_trend`,
  `range_yearly_magnitude`,
  `complementary_favourable_range`,
  `coverage_surface_area`,
  `percentage_coverage_surface_area`,
  `coverage_trend`,
  `coverage_yearly_magnitude`,
  `complementary_favourable_area`,
  `conclusion_range`,
  `conclusion_range_gis`,
  `conclusion_coverage`,
  `conclusion_coverage_gis`,
  `percentage_structure`,
  `conclusion_structure`,
  `percentage_future`,
  `conclusion_future`,
  `percentage_assessment`,
  `conclusion_assessment`,
  `range_grid_area`,
  `percentage_range_grid_area`,
  `distribution_grid_area`,
  `percentage_distribution_grid_area`,
  `assessment_needed`
FROM 
  `etc_data_habitattype_automatic_assessment`
WHERE <dtml-sqltest habitatcode type=string>
<dtml-if region>
	AND <dtml-sqltest region type=string>
</dtml-if>
ORDER BY `etc_data_habitattype_automatic_assessment`.`order`, region