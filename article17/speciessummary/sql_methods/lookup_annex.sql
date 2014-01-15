-- Z SQL Method
-- /article17/speciessummary/sql_methods/lookup_annex
<params>assesment_speciesname</params>
SELECT distinct `annex_II`,`priority`,`annex_IV`,`annex_V`
FROM `etc_data_species_regions` 
WHERE <dtml-sqltest assesment_speciesname type="string">