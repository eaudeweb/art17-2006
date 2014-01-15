-- Z SQL Method
-- /article17/habitatsummary/sql_methods/get_method_details
<params>method</params>
SELECT 
  `details`
FROM 
  `etc_dic_method`
WHERE <dtml-sqltest method type=string>