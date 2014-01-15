-- Z SQL Method
-- /article17/habitatsummary/sql_methods/lookup_habitat_name
<params>habitatcode</params>
SELECT * 
FROM `etc_dic_hd_habitats` 
WHERE <dtml-sqltest name="habitatcode" column="habcode" type=string>