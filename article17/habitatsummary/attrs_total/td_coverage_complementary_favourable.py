# Script (Python)
# /article17/habitatsummary/attrs_total/td_coverage_complementary_favourable
# params: 'record'
## Script (Python) "td_coverage_complementary_favourable"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record
##title=
##
trend = context.parse_semicolon(record['complementary_favourable_area'])
return {
    'class': 'center section-border',
    'content': context.str2num(trend, '')
    }
