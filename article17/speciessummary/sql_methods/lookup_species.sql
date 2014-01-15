-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_species
<params>assesment_speciesname
bioregion</params>
SELECT 
  `species_type`,
  `species_type_asses`,
  `eu_country_code`,
  `assesment_speciesname`,
  `region`,
  `envelope`,
  `filename`,
  `range_surface_area`,
  `percentage_range_surface_area`,
  `conclusion_range`,
  `percentage_range_grid_area`,
  `range_trend`,
  `range_yearly_magnitude`,
  `complementary_favourable_range_q`,
  `complementary_favourable_range`,
  `population_minimum_size`,
  `population_maximum_size`,
  `population_size_unit`,
  `filled_population`,
  `percentage_population_mean_size`,
  `conclusion_population`,
  `percentage_distribution_grid_area`,
  `population_trend`,
  `population_yearly_magnitude`,
  `complementary_favourable_population_q`,
  `complementary_favourable_population`,
  `filled_complementary_favourable_population`,
  `habitat_surface_area`,  
  `percentage_habitat_surface_area`,
  `conclusion_habitat`,
  `distribution_grid_area`,
  `habitat_trend`,
  `complementary_suitable_habitat`,
  `future_prospects`,
  `conclusion_future`,
  `conclusion_assessment`,
  `range_grid_area`,
  `range_quality`,
  `population_quality`,
  `habitat_quality`,
  `species_name_different`,
  `complementary_other_information`,
  `complementary_other_information_english`,
  `speciesname`
FROM 
  `etc_data_species_regions`
WHERE <dtml-sqltest assesment_speciesname type=string>
<dtml-if bioregion>
AND <dtml-sqltest name="bioregion" column="region" type=string>
</dtml-if>
ORDER BY region, species_type_asses, eu_country_code