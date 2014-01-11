# Script (Python)
# /article17/speciessummary/attrs_total/td_population_size_unit
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
size = context.parse_semicolon(record['population_size']) or ''
return {
    'class': 'number',
    'content': size
    }
