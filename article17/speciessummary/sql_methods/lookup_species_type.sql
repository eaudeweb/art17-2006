-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_species_type
<params>abbrev</params>
SELECT 
  `SpeciesType`
FROM 
  `etc_dic_species_type`
WHERE <dtml-sqltest abbrev type=string>