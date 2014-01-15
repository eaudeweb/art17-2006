-- Z SQL Method
-- /article17/habitatsummary/sql_methods/select_group_habitats
<params>group</params>
SELECT DISTINCT 
  etc_data_habitattype_regions.habitatcode,
  `etc_dic_hd_habitats`.`shortname`
FROM
  etc_data_habitattype_regions
INNER JOIN 
  etc_dic_hd_habitats ON (`etc_data_habitattype_regions`.`habitatcode` = `etc_dic_hd_habitats`.`habcode`)
WHERE
  <dtml-sqltest name="group" column="etc_data_habitattype_regions.group" type=string>