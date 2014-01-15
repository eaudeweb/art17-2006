# Script (Python)
# /article17/habitatsummary/attrs_total/td_coverage_yearly_magnitude
# params: 'record'
## Script (Python) "td_coverage_yearly_magnitude"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record
##title=
##
trend = context.parse_semicolon(record['coverage_yearly_magnitude'])
return {
    'class': 'number',
    'content': context.str2num(trend, '')
    }
