-- Z SQL Method
-- /article17/habitatsummary/sql_methods/update_user_habitat_manual_assesment
<params>MS
region
habitatcode
range_surface_area
range_trend
range_yearly_magnitude
coverage_yearly_magnitude
complementary_favourable_range
coverage_surface_area
coverage_trend
complementary_favourable_area
method_range
conclusion_range
method_area
conclusion_area
method_structure
conclusion_structure
method_future
conclusion_future
method_assessment
conclusion_assessment
user
last_update
deleted_record
decision</params>
UPDATE 
  `habitattypes_manual_assessment`
SET `range_surface_area` = <dtml-sqlvar range_surface_area type=string>,
  `range_trend` = <dtml-sqlvar range_trend type=string>,
  `range_yearly_magnitude` = <dtml-sqlvar range_yearly_magnitude type=string>,
  `coverage_yearly_magnitude` = <dtml-sqlvar coverage_yearly_magnitude type=string>,
  `complementary_favourable_range` = <dtml-sqlvar complementary_favourable_range type=string>,
  `coverage_surface_area` = <dtml-sqlvar coverage_surface_area type=string>,
  `coverage_trend` = <dtml-sqlvar coverage_trend type=string>,
  `complementary_favourable_area` = <dtml-sqlvar complementary_favourable_area type=string>,
  `method_range` = <dtml-sqlvar method_range type=string>,
  `conclusion_range` = <dtml-sqlvar conclusion_range type=string>,
  `method_area` = <dtml-sqlvar method_area type=string>,
  `conclusion_area` = <dtml-sqlvar conclusion_area type=string>,
  `method_structure` = <dtml-sqlvar method_structure type=string>,
  `conclusion_structure` = <dtml-sqlvar conclusion_structure type=string>,
  `method_future` = <dtml-sqlvar method_future type=string>,
  `conclusion_future` = <dtml-sqlvar conclusion_future type=string>,
  `method_assessment` = <dtml-sqlvar method_assessment type=string>,
  `conclusion_assessment` = <dtml-sqlvar conclusion_assessment type=string>,
  `last_update` = <dtml-sqlvar last_update type=string>,
  `decision` = <dtml-sqlvar decision type=string>
WHERE 
  `region` = <dtml-sqlvar region type=string> 
AND 
  `habitatcode` = <dtml-sqlvar habitatcode type=string>
AND `user` = <dtml-sqlvar user type=string>
AND `MS` = <dtml-sqlvar MS type=string>