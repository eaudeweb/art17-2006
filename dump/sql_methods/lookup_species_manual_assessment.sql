-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_species_manual_assessment
<params>speciesname
bioregion</params>
SELECT *
FROM 
  `species_manual_assessment`
WHERE <dtml-sqltest name="speciesname" column="assesment_speciesname" type=string>
<dtml-if bioregion>
	AND <dtml-sqltest name="bioregion" column="region" type=string>
</dtml-if>
ORDER BY deleted_record, last_update, region