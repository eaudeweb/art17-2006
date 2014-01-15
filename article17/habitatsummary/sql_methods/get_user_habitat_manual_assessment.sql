-- Z SQL Method
-- /article17/habitatsummary/sql_methods/get_user_habitat_manual_assessment
<params>habitatcode
region
user
ms
</params>
SELECT 
  `region`,
  `MS`,
  `habitatcode`,
  `range_surface_area`,
  `range_trend`,
  `range_yearly_magnitude`,
  `coverage_yearly_magnitude`,
  `complementary_favourable_range`,
  `coverage_surface_area`,
  `coverage_trend`,
  `complementary_favourable_area`,
  `method_range`,
  `conclusion_range`,
  `method_area`,
  `conclusion_area`,
  `method_structure`,
  `conclusion_structure`,
  `method_future`,
  `conclusion_future`,
  `method_assessment`,
  `conclusion_assessment`,
  `user`,
  `last_update`,
  `deleted_record`,
  `decision`,
  `user_decision`,
  `last_update_decision`
FROM 
  `habitattypes_manual_assessment`
WHERE <dtml-sqltest habitatcode type=string>
AND <dtml-sqltest region type=string>
AND <dtml-sqltest user type=string>
AND <dtml-sqltest name="ms" column="MS" type=string>