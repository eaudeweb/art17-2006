# Script (Python)
# /article17/habitatsummary/getHabitatRegions
# params: 'habitat'
## Script (Python) "getHabitatRegions"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=habitat
##title=
##
# Example code:

records = [rec['region'] for rec in context.sql_methods.select_habitat_regions(habitatcode=habitat)]
regions = ['%s,%s' % (context.sql_methods.lookup_bioregion().get(r,''), r) for r in records]

#first option must be blank
regions.append('All bioregions,')
regions.sort()
regions.reverse()

return ';'.join(regions)
