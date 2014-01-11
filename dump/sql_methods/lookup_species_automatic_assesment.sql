-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_species_automatic_assesment
<params>assesment_speciesname
bioregion</params>
SELECT 
  `assessment_method`,
  `order`,
  `region`,
  `assesment_speciesname`,
  `range_surface_area`,
  `percentage_range_surface_area`,
  `range_trend`,
  `range_yearly_magnitude`,
  `complementary_favourable_range`,
  `population_size`,
  `percentage_population_mean_size`,
  `population_trend`,
  `population_yearly_magnitude`,
  `complementary_favourable_population`,
  `habitat_surface_area`,
  `percentage_habitat_surface_area`,
  `habitat_trend`,
  `complementary_suitable_habitat`,
  `percentage_future`,
  `conclusion_range`,
  `conclusion_range_gis`,
  `conclusion_population`,
  `conclusion_population_gis`,
  `conclusion_habitat`,
  `conclusion_habitat_gis`,
  `conclusion_future`,
  `conclusion_assessment`,
  `range_grid_area`,
  `percentage_range_grid_area`,
  `distribution_grid_area`,
  `percentage_assessment`,
  `percentage_distribution_grid_area`
FROM 
  `etc_data_species_automatic_assessment`
WHERE <dtml-sqltest assesment_speciesname type=string>
<dtml-if bioregion>
AND <dtml-sqltest name="bioregion" column="region" type=string>
</dtml-if>
ORDER BY `etc_data_species_automatic_assessment`.order, region