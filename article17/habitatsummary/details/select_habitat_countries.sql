-- Z SQL Method
-- /article17/habitatsummary/details/select_habitat_countries
<params>region
Habitatcode</params>
SELECT
  eu_country_code,
  code,
  conclusion_assessment,
  region
FROM
  etc_data_habitattype_regions
WHERE <dtml-sqltest region type="string" multiple="multiple">
AND <dtml-sqltest Habitatcode type=string>