-- Z SQL Method
-- /article17/habitatsummary/sql_methods/lookup_habitat_type
<params>abbrev</params>
SELECT 
  `SpeciesType`
FROM 
  `etc_dic_species_type`
WHERE <dtml-sqltest abbrev type=string>