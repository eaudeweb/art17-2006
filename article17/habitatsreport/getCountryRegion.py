# Script (Python)
# /article17/habitatsreport/getCountryRegion
# params: 'country'
## Script (Python) "getCountryRegion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=country
##title=
##
records = [rec['region'] for rec in context.sql_methods.lookup_country_bioregion(country=country)]
regions = ['%s,%s' % (context.sql_methods.lookup_bioregion().get(r,''), r) for r in records]

#first option must be blank
regions.append(',')
regions.sort()
regions.reverse()

return ';'.join(regions)
