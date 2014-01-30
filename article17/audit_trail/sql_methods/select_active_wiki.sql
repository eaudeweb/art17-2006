-- Z SQL Method
-- /article17/wiki_trail/sql_methods/select_active_wiki
<params>region
assesment_speciesname
habitat</params>
SELECT 
  wiki_trail.id,
  wiki_trail_changes.body,
  wiki_trail_changes.changed
FROM
  wiki_trail_changes
  INNER JOIN wiki_trail ON (wiki_trail_changes.wiki_id = wiki_trail.id)
WHERE <dtml-sqltest region type=string>
<dtml-if assesment_speciesname>
	AND <dtml-sqltest assesment_speciesname type=string>
</dtml-if>
<dtml-if habitat>
	AND <dtml-sqltest name="habitat" column="habitatcode" type=string>
</dtml-if>
AND wiki_trail_changes.active = 1