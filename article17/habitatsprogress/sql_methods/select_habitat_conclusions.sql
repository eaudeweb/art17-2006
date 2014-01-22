-- Z SQL Method
-- /article17/habitatsprogress/sql_methods/select_habitat_conclusions
<params>conclusion
group</params>
SELECT `habitattypes_manual_assessment`.`habitatcode`,
   `etc_dic_hd_habitats`.`shortname`,
<dtml-if "conclusion == 'conclusion_range'">
  `habitattypes_manual_assessment`.`method_range` as method,
  `habitattypes_manual_assessment`.`conclusion_range` as conclusion,
<dtml-elif "conclusion == 'conclusion_area'">
  `habitattypes_manual_assessment`.`method_area` as method,
  `habitattypes_manual_assessment`.`conclusion_area` as conclusion,
<dtml-elif "conclusion == 'conclusion_future'">
  `habitattypes_manual_assessment`.`method_future` as method,
  `habitattypes_manual_assessment`.`conclusion_future` as conclusion,
<dtml-elif "conclusion == 'conclusion_structure'">
  `habitattypes_manual_assessment`.`method_structure` as method,
  `habitattypes_manual_assessment`.`conclusion_structure` as conclusion,
<dtml-elif "conclusion == 'conclusion_assessment'">
  `habitattypes_manual_assessment`.`method_assessment` as method,
  `habitattypes_manual_assessment`.`conclusion_assessment` as conclusion,
  `habitattypes_manual_assessment`.`conclusion_range`,
  `habitattypes_manual_assessment`.`method_range`,
</dtml-if>
  `etc_dic_biogeoreg`.`order`,
  `etc_dic_biogeoreg`.`reg_code`,
  `habitattypes_manual_assessment`.`decision`,
  `habitattypes_manual_assessment`.`region`,
  `habitattypes_manual_assessment`.`user`,
  `habitattypes_manual_assessment`.`method_assessment`,
  `etc_dic_method`.`details` as method_details,
  `etc_dic_decision`.`details` as decision_details,
  `habitat_group`.`group`
FROM 
  `habitattypes_manual_assessment`
INNER JOIN `etc_dic_biogeoreg` ON (`habitattypes_manual_assessment`.`region` = `etc_dic_biogeoreg`.`reg_code`)
INNER JOIN `habitat_group` ON (`habitattypes_manual_assessment`.`habitatcode` = `habitat_group`.`habitatcode`)
INNER JOIN `etc_dic_hd_habitats` ON (`habitattypes_manual_assessment`.`habitatcode` = `etc_dic_hd_habitats`.`habcode`)
<dtml-if "conclusion == 'conclusion_range'">
INNER JOIN `etc_dic_method` ON (`habitattypes_manual_assessment`.`method_range` = `etc_dic_method`.`method`)
<dtml-elif "conclusion == 'conclusion_area'">
INNER JOIN `etc_dic_method` ON (`habitattypes_manual_assessment`.`method_area` = `etc_dic_method`.`method`)
<dtml-elif "conclusion == 'conclusion_future'">
INNER JOIN `etc_dic_method` ON (`habitattypes_manual_assessment`.`method_future` = `etc_dic_method`.`method`)
<dtml-elif "conclusion == 'conclusion_structure'">
INNER JOIN `etc_dic_method` ON (`habitattypes_manual_assessment`.`method_structure` = `etc_dic_method`.`method`)
<dtml-elif "conclusion == 'conclusion_assessment'">
INNER JOIN `etc_dic_method` ON (`habitattypes_manual_assessment`.`method_assessment` = `etc_dic_method`.`method`)
</dtml-if>
LEFT JOIN `etc_dic_decision` ON (`habitattypes_manual_assessment`.`decision` = `etc_dic_decision`.`decision`)
WHERE <dtml-sqltest name="group" column="habitat_group.group" type=string>