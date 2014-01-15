# Script (Python)
# /article17/speciessummary/attrs_total/td_habitat_area
# params: 'record'
## Script (Python) "td_habitat_area"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record
##title=
##
return {
    'class': 'number',
    'content': context.str2num(context.parse_semicolon(record['habitat_surface_area']), '')
    }
