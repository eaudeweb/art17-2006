-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_decision
<params></params>
SELECT 
  `order`,
  `decision`,
  `details`
FROM 
  `etc_dic_decision`
ORDER BY `decision`