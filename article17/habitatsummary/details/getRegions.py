# Script (Python)
# /article17/habitatsummary/details/getRegions
# params: 'habitat'
## Script (Python) "getRegions"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=habitat
##title=
##
regions = ['^%s' % rec['region'] for rec in context.sql_methods.select_habitat_regions(habitatcode=habitat)]
return '|'.join(regions)
