-- Z SQL Method
-- /article17/wiki/sql_methods/insert_wiki
<params>region
assesment_speciesname
habitatcode
body
editor</params>
INSERT INTO 
  `wiki`
(
  `region`,
  `assesment_speciesname`,
  `habitatcode`
) 
VALUE (
  <dtml-sqlvar region type=string>,
  <dtml-sqlvar assesment_speciesname type=string>,
  <dtml-sqlvar habitatcode type=string>
)

<dtml-var sql_delimiter>
SELECT LAST_INSERT_ID() AS newid