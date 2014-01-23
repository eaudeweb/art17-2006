-- Z SQL Method
-- /article17/speciesreport/sql_methods/lookup_conclusions
<params></params>
SELECT 
  `order`,
  `conclusion`,
  `details`
FROM 
  `etc_dic_conclusion`
ORDER BY conclusion