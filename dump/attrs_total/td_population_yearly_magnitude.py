# Script (Python)
# /article17/speciessummary/attrs_total/td_population_yearly_magnitude
# params: 'record'
## Script (Python) "td_population_yearly_magnitude"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record
##title=
##
range = context.parse_semicolon(record['population_yearly_magnitude'])
return {
    'class': 'number',
    'content': context.str2num(range, '')
    }
