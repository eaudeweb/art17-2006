-- Z SQL Method
-- /article17/habitatsummary/sql_methods/select_habitat_regions
<params>habitatcode</params>
SELECT DISTINCT 
  etc_data_habitattype_regions.region
FROM
  etc_data_habitattype_regions
WHERE <dtml-sqltest name="habitatcode" column="etc_data_habitattype_regions.habitatcode" type=string>