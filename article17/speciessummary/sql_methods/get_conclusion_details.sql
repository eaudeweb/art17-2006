-- Z SQL Method
-- /article17/speciessummary/sql_methods/get_conclusion_details
<params>decision</params>
SELECT 
  `details`
FROM 
  `etc_dic_decision`
WHERE <dtml-sqltest decision type=string>