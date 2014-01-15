# Script (Python)
# /article17/speciessummary/attrs_total/td_habitat_complementary_suitable
# params: 'record'
## Script (Python) "td_habitat_complementary_suitable"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record
##title=
##
habitat = context.parse_semicolon(record['complementary_suitable_habitat'])
return {
    'class': 'number section-border',
    'content': context.str2num(habitat, '')
    }
