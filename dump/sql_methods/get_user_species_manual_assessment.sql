-- Z SQL Method
-- /article17/speciessummary/sql_methods/get_user_species_manual_assessment
<params>assesment_speciesname
region
user
ms
</params>
SELECT
  `MS`,
  `region`,
  `assesment_speciesname`,
  `range_surface_area`,
  `method_range`,
  `range_trend`,
  `range_yearly_magnitude`,
  `complementary_favourable_range`,
  `population_size`,
  `population_size_unit`,
  `method_population`,
  `population_trend`,
  `population_yearly_magnitude`,
  `complementary_favourable_population`,
  `habitat_surface_area`,
  `method_habitat`,
  `habitat_trend`,
  `complementary_suitable_habitat`,
  `conclusion_range`,
  `conclusion_population`,
  `conclusion_habitat`,
  `conclusion_future`,
  `method_future`,
  `conclusion_assessment`,
  `method_assessment`,
  `user`,
  `last_update`,
  `deleted_record`,
  `decision`,
  `user_decision`,
  `last_update_decision`
FROM 
  `species_manual_assessment`
WHERE <dtml-sqltest assesment_speciesname type=string>
AND <dtml-sqltest region type=string>
AND <dtml-sqltest user type=string>
<dtml-if ms>
	AND <dtml-sqltest name="ms" column="MS" type=string>
</dtml-if>