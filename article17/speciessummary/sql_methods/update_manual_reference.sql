-- Z SQL Method
-- /article17/speciessummary/sql_methods/update_manual_reference
<params>region
assesment_speciesname
complementary_favourable_range
complementary_favourable_population
user</params>
UPDATE 
  species_manual_assessment
SET 
  complementary_favourable_range = <dtml-sqlvar complementary_favourable_range type=string>,
  complementary_favourable_population = <dtml-sqlvar complementary_favourable_population type=string>
WHERE region = <dtml-sqlvar region type=string> 
AND assesment_speciesname = <dtml-sqlvar assesment_speciesname type=string>
AND user = <dtml-sqlvar user type=string>