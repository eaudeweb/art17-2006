-- Z SQL Method
-- /article17/habitatsummary/sql_methods/insert_habitat_manual_assesment
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
decision
user_decision
last_update_decision</params>
INSERT INTO 
  `habitattypes_manual_assessment`
(
  `MS`,
  `region`,
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
) 
VALUE (
  <dtml-sqlvar MS type=string>,
  <dtml-sqlvar region type=string>,
  <dtml-sqlvar habitatcode type=string>,
  <dtml-sqlvar range_surface_area type=string>,
  <dtml-sqlvar range_trend type=string>,
  <dtml-sqlvar range_yearly_magnitude type=string>,
  <dtml-sqlvar coverage_yearly_magnitude type=string>,
  <dtml-sqlvar complementary_favourable_range type=string>,
  <dtml-sqlvar coverage_surface_area type=string>,
  <dtml-sqlvar coverage_trend type=string>,
  <dtml-sqlvar complementary_favourable_area type=string>,
  <dtml-sqlvar method_range type=string>,
  <dtml-sqlvar conclusion_range type=string>,
  <dtml-sqlvar method_area type=string>,
  <dtml-sqlvar conclusion_area type=string>,
  <dtml-sqlvar method_structure type=string>,
  <dtml-sqlvar conclusion_structure type=string>,
  <dtml-sqlvar method_future type=string>,
  <dtml-sqlvar conclusion_future type=string>,
  <dtml-sqlvar method_assessment type=string>,
  <dtml-sqlvar conclusion_assessment type=string>,
  <dtml-sqlvar user type=string>,
  <dtml-sqlvar last_update type=string>,
  <dtml-sqlvar deleted_record type=string>,
  <dtml-sqlvar decision type=string>,
  <dtml-sqlvar user_decision type=string>,
  <dtml-sqlvar last_update_decision type=string>
);