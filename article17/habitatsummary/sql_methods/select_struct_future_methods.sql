-- Z SQL Method
-- /article17/habitatsummary/sql_methods/select_struct_future_methods
<params></params>
SELECT 
  `order`,
  `method`,
  `details`
FROM 
  `etc_dic_method`
WHERE (`method` LIKE '2%' and `method` != '2XP') or method =''
ORDER BY method