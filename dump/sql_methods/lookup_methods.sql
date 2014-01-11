-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_methods
<params></params>
SELECT 
  `order`,
  `method`,
  `details`
FROM 
  `etc_dic_method`
WHERE `method` LIKE '1%' or (`method` LIKE '2%' and `method` != '2XA') or method =''
ORDER BY method