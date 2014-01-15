-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_assesment_methods
<params></params>
SELECT 
  `order`,
  `method`,
  `details`
FROM 
  `etc_dic_method`
WHERE (`method` LIKE '3%' and `method`!='3XA') or `method`='MTX' or method =''
ORDER BY method