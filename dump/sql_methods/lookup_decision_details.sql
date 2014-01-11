-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_decision_details
<params>decision</params>
SELECT `details` FROM `etc_dic_decision` WHERE <dtml-sqltest decision type=string>