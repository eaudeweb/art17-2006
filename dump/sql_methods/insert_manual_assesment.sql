-- Z SQL Method
-- /article17/speciessummary/sql_methods/insert_manual_assesment
<params>MS
region
assesment_speciesname
range_surface_area
method_range
range_trend
range_yearly_magnitude
complementary_favourable_range
population_size
population_size_unit
method_population
population_trend
population_yearly_magnitude
complementary_favourable_population
habitat_surface_area
method_habitat
habitat_trend
complementary_suitable_habitat
conclusion_range
conclusion_population
conclusion_habitat
conclusion_future
method_future
method_assessment
conclusion_assessment
user
last_update
deleted_record
decision
user_decision
last_update_decision</params>
INSERT INTO 
  species_manual_assessment
(MS,
  region,
  assesment_speciesname,
  range_surface_area,
  method_range,
  range_trend,
  range_yearly_magnitude,
  complementary_favourable_range,
  population_size,
  population_size_unit,
  method_population,
  population_trend,
  population_yearly_magnitude,
  complementary_favourable_population,
  habitat_surface_area,
  method_habitat,
  habitat_trend,
  complementary_suitable_habitat,
  conclusion_range,
  conclusion_population,
  conclusion_habitat,
  conclusion_future,
  method_future,
  method_assessment,
  conclusion_assessment,
  user,
  last_update,
  deleted_record,
  decision,
  user_decision,
  last_update_decision
) 
VALUE (
  <dtml-sqlvar MS type=string>,
  <dtml-sqlvar region type=string>,
  <dtml-sqlvar assesment_speciesname type=string>,
  <dtml-sqlvar range_surface_area type=string>,
  <dtml-sqlvar method_range type=string>,
  <dtml-sqlvar range_trend type=string>,
  <dtml-sqlvar range_yearly_magnitude type=string>,
  <dtml-sqlvar complementary_favourable_range type=string>,
  <dtml-sqlvar population_size type=string>,
  <dtml-sqlvar population_size_unit type=string>,
  <dtml-sqlvar method_population type=string>,
  <dtml-sqlvar population_trend type=string>,
  <dtml-sqlvar population_yearly_magnitude type=string>,
  <dtml-sqlvar complementary_favourable_population type=string>,
  <dtml-sqlvar habitat_surface_area type=string>,
  <dtml-sqlvar method_habitat type=string>,
  <dtml-sqlvar habitat_trend type=string>,
  <dtml-sqlvar complementary_suitable_habitat type=string>,
  <dtml-sqlvar conclusion_range type=string>,
  <dtml-sqlvar conclusion_population type=string>,
  <dtml-sqlvar conclusion_habitat type=string>,
  <dtml-sqlvar conclusion_future type=string>,
  <dtml-sqlvar method_future type=string>,
  <dtml-sqlvar method_assessment type=string>,
  <dtml-sqlvar conclusion_assessment type=string>,
  <dtml-sqlvar user type=string>,
  <dtml-sqlvar last_update type=string>,
  <dtml-sqlvar deleted_record type=int>,
  <dtml-sqlvar decision type=string>,
  <dtml-sqlvar user_decision type=string>,
  <dtml-sqlvar last_update_decision type=string>
)