-- Z SQL Method
-- /article17/wiki/sql_methods/insert_wiki_changes
<params>id
body
editor
active</params>
INSERT INTO 
  `wiki_changes`
(
  `wiki_id`,
  `body`,
  `editor`,
  `active`
) 
VALUE (
  <dtml-sqlvar id type=string>,
  <dtml-sqlvar body type=string>,
  <dtml-sqlvar editor type=string>,
  <dtml-sqlvar active type=string>
)