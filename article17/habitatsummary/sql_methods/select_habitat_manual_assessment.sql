-- Z SQL Method
-- /article17/habitatsummary/sql_methods/select_habitat_manual_assessment
<params>habitatcode
region</params>
SELECT * FROM 
  `habitattypes_manual_assessment`
WHERE <dtml-sqltest habitatcode type=string>
<dtml-if region>
	AND <dtml-sqltest region type=string>
</dtml-if>