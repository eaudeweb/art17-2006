-- Z SQL Method
-- /article17/habitatsprogress/sql_methods/lookup_habitat_name
<params>habitatcode</params>
SELECT 
  `priority`,
  `shortname`
FROM 
  `etc_dic_hd_habitats`
WHERE <dtml-sqltest name="habitatcode" column="habcode" type=string>