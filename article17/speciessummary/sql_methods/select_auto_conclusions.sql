-- Z SQL Method
-- /article17/speciessummary/sql_methods/select_auto_conclusions
<params>assesment_speciesname
bioregion</params>
SELECT decision
FROM `species_manual_assessment`
WHERE <dtml-sqltest assesment_speciesname type=string>
AND <dtml-sqltest name="bioregion" column="region" type=string>
AND user = 'maximiur' or user = 'iurieetcbd'