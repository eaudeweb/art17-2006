-- Z SQL Method
-- /article17/habitatsummary/sql_methods/select_habitat_annexes
<params>habitatcode</params>
SELECT DISTINCT `annex`, priority
FROM `etc_data_habitattype_regions` 
WHERE <dtml-sqltest habitatcode type="string">