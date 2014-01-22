-- Z SQL Method
-- /article17/habitatsprogress/sql_methods/select_groups
<params></params>
SELECT DISTINCT `etc_data_habitattype_regions`.`group` as upper_group 
FROM `etc_data_habitattype_regions`
ORDER BY `etc_data_habitattype_regions`.`habitatcode`