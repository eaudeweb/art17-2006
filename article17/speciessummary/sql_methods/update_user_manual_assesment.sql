-- Z SQL Method
-- /article17/speciessummary/sql_methods/update_user_manual_assesment
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
decision
</params>
UPDATE 
  species_manual_assessment
SET 
  range_surface_area = <dtml-sqlvar range_surface_area type=string>,
  method_range = <dtml-sqlvar method_range type=string>,
  range_trend = <dtml-sqlvar range_trend type=string>,
  range_yearly_magnitude = <dtml-sqlvar range_yearly_magnitude type=string>,
  complementary_favourable_range = <dtml-sqlvar complementary_favourable_range type=string>,
  population_size = <dtml-sqlvar population_size type=string>,
  population_size_unit = <dtml-sqlvar population_size_unit type=string>,
  method_population = <dtml-sqlvar method_population type=string>,
  population_trend = <dtml-sqlvar population_trend type=string>,
  population_yearly_magnitude = <dtml-sqlvar population_yearly_magnitude type=string>,
  complementary_favourable_population = <dtml-sqlvar complementary_favourable_population type=string>,
  habitat_surface_area = <dtml-sqlvar habitat_surface_area type=string>,
  method_habitat = <dtml-sqlvar method_habitat type=string>,
  habitat_trend = <dtml-sqlvar habitat_trend type=string>,
  complementary_suitable_habitat = <dtml-sqlvar complementary_suitable_habitat type=string>,
  conclusion_range = <dtml-sqlvar conclusion_range type=string>,
  conclusion_population = <dtml-sqlvar conclusion_population type=string>,
  conclusion_habitat = <dtml-sqlvar conclusion_habitat type=string>,
  conclusion_future = <dtml-sqlvar conclusion_future type=string>,
  method_future = <dtml-sqlvar method_future type=string>,
  method_assessment = <dtml-sqlvar method_assessment type=string>,
  conclusion_assessment = <dtml-sqlvar conclusion_assessment type=string>,
  last_update = <dtml-sqlvar last_update type=string>,
  decision = <dtml-sqlvar decision type=string>
WHERE region = <dtml-sqlvar region type=string> 
AND assesment_speciesname = <dtml-sqlvar assesment_speciesname type=string>
AND user = <dtml-sqlvar user type=string>
AND MS =  <dtml-sqlvar MS type=string>