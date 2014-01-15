# Script (Python)
# /article17/habitatsummary/attrs_total/td_coverage_trend
# params: 'record'
## Script (Python) "td_coverage_trend"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record
##title=
##
trend = context.parse_semicolon(record['coverage_trend']) or ''
return {
    'class': 'center',
    'content': trend
    }
