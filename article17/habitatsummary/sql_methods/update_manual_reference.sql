-- Z SQL Method
-- /article17/habitatsummary/sql_methods/update_manual_reference
<params>region
habitatcode
complementary_favourable_range
complementary_favourable_area
user</params>
UPDATE 
  `habitattypes_manual_assessment`
SET `complementary_favourable_range` = <dtml-sqlvar complementary_favourable_range type=string>,
  `complementary_favourable_area` = <dtml-sqlvar complementary_favourable_area type=string>
WHERE 
  `region` = <dtml-sqlvar region type=string> 
AND 
  `habitatcode` = <dtml-sqlvar habitatcode type=string>
AND `user` = <dtml-sqlvar user type=string>