# Script (Python)
# /article17/habitatsummary/attrs_conclusion/td_range_yearly_magnitude
# params: 'record'
## Script (Python) "td_range_yearly_magnitude"
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
    'content': context.str2num(record['range_yearly_magnitude'], '')
    }
