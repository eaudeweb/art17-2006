# Script (Python)
# /article17/speciessummary/attrs_conclusion/td_habitat_trend
# params: 'record'
## Script (Python) "td_habitat_trend"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record
##title=
##
trend = record['habitat_trend'] or ''
return {
    'class': 'center',
    'content': trend
    }
