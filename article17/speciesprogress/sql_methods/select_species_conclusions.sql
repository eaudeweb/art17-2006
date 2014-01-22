-- Z SQL Method
-- /article17/speciesprogress/sql_methods/select_species_conclusions
<params>conclusion
group</params>
SELECT
  `species_manual_assessment`.`assesment_speciesname`,
<dtml-if "conclusion == 'conclusion_range'">
  `species_manual_assessment`.`conclusion_range` as conclusion,
  `species_manual_assessment`.`method_range` as method,
<dtml-elif "conclusion == 'conclusion_population'">
  `species_manual_assessment`.`conclusion_population` as conclusion,
  `species_manual_assessment`.`method_population` as method,
<dtml-elif "conclusion == 'conclusion_habitat'">
  `species_manual_assessment`.`conclusion_habitat` as conclusion,
  `species_manual_assessment`.`method_habitat` as method,
<dtml-elif "conclusion == 'conclusion_future'">
  `species_manual_assessment`.`conclusion_future` as conclusion,
  `species_manual_assessment`.`method_future` as method,
<dtml-elif "conclusion == 'conclusion_assessment'">
  `species_manual_assessment`.`conclusion_assessment` as conclusion,
  `species_manual_assessment`.`method_assessment` as method,
  `species_manual_assessment`.`conclusion_range`,
  `species_manual_assessment`.`method_range`,
</dtml-if>
  `etc_dic_biogeoreg`.`order`,
  `etc_dic_biogeoreg`.`reg_code`,
  `species_manual_assessment`.`decision`,
  `species_manual_assessment`.`region`,
  `species_manual_assessment`.`user`,
  `species_manual_assessment`.`method_assessment`,
  `etc_dic_method`.`details` as method_details,
  `etc_dic_decision`.`details` as decision_details,
  `species_group`.`group`
FROM species_manual_assessment
INNER JOIN `etc_dic_biogeoreg` ON (`species_manual_assessment`.`region` = `etc_dic_biogeoreg`.`reg_code`)
INNER JOIN `species_group` ON (`species_manual_assessment`.`assesment_speciesname` = `species_group`.`assesment_speciesname`)
<dtml-if "conclusion == 'conclusion_range'">
INNER JOIN `etc_dic_method` ON (`species_manual_assessment`.`method_range` = `etc_dic_method`.`method`)
<dtml-elif "conclusion == 'conclusion_population'">
INNER JOIN `etc_dic_method` ON (`species_manual_assessment`.`method_population` = `etc_dic_method`.`method`)
<dtml-elif "conclusion == 'conclusion_habitat'">
INNER JOIN `etc_dic_method` ON (`species_manual_assessment`.`method_habitat` = `etc_dic_method`.`method`)
<dtml-elif "conclusion == 'conclusion_future'">
INNER JOIN `etc_dic_method` ON (`species_manual_assessment`.`method_future` = `etc_dic_method`.`method`)
<dtml-elif "conclusion == 'conclusion_assessment'">
INNER JOIN `etc_dic_method` ON (`species_manual_assessment`.`method_assessment` = `etc_dic_method`.`method`)
</dtml-if>
LEFT JOIN `etc_dic_decision` ON (`species_manual_assessment`.`decision` = `etc_dic_decision`.`decision`)
WHERE <dtml-sqltest name="group" column="species_group.group" type=string>
