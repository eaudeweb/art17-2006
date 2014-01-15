-- Z SQL Method
-- /article17/habitatsummary/sql_methods/select_assesment_methods
<params></params>
SELECT 
  `order`,
  `method`,
  `details`
FROM 
  `etc_dic_method`
WHERE (`method` LIKE '3%' and `method`!='3XP') or `method`='MTX' or method =''
ORDER BY method