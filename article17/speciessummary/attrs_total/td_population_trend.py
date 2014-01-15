# Script (Python)
# /article17/speciessummary/attrs_total/td_population_trend
# params: 'record'
## Script (Python) "td_population_trend"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record
##title=
##
trend = context.parse_semicolon(record['population_trend']) or ''
return {
    'class': 'center',
    'content': trend
    }
