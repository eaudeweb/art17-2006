# Script (Python)
# /article17/speciessummary/attrs_conclusion/td_population_yearly_magnitude
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
return {
    'class': 'center',
    'content': context.str2num(record['population_yearly_magnitude'], '')
    }
