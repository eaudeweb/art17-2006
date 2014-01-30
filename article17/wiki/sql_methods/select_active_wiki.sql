-- Z SQL Method
-- /article17/wiki/sql_methods/select_active_wiki
<params>region
assesment_speciesname
habitat</params>
SELECT 
  wiki.id,
  wiki_changes.body,
  wiki_changes.changed
FROM
  wiki_changes
  INNER JOIN wiki ON (wiki_changes.wiki_id = wiki.id)
WHERE <dtml-sqltest region type=string>
<dtml-if assesment_speciesname>
	AND <dtml-sqltest assesment_speciesname type=string>
</dtml-if>
<dtml-if habitat>
	AND <dtml-sqltest name="habitat" column="habitatcode" type=string>
</dtml-if>
AND wiki_changes.active = 1