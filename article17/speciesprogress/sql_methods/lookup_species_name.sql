-- Z SQL Method
-- /article17/speciesprogress/sql_methods/lookup_species_name
<params>species</params>
SELECT DISTINCT
  `priority`
FROM 
  `species_name`
WHERE <dtml-sqltest name="species" column="assesment_speciesname" type=string>