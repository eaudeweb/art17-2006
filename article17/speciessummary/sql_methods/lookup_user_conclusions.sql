-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_user_conclusions
<params>bioregion
speciesname
username</params>
SELECT
  `user`, MS
FROM 
  `species_manual_assessment`
WHERE
  <dtml-sqltest name="bioregion" column="region" type=string>
AND <dtml-sqltest name="speciesname" column="assesment_speciesname" type=string>
AND <dtml-sqltest name="username" column="user" type=string>