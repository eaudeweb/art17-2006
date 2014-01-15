# Script (Python)
# /article17/speciessummary/attrs_total/td_population_complementary_favourable
# params: 'record'
## Script (Python) "td_population_complementary_favourable"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record
##title=
##
range = context.parse_semicolon(record['complementary_favourable_population'])
return {
    'class': 'number section-border',
    'content': context.str2num(range, '')
    }
