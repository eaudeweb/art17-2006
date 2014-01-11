# Script (Python)
# /article17/speciessummary/attrs_conclusion/td_population_size_unit
# params: 'record'
## Script (Python) "td_population_size_unit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record
##title=
##
size = record['population_size'] or ''
unit = record['population_size_unit'] or ''
return {
    'class': 'number',
    'content': "%s %s" % (size, unit)
    }
