# Script (Python)
# /article17/speciessummary/attrs_conclusion/td_range_surface
# params: 'record'
## Script (Python) "td_range_surface"
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
    'content': context.str2num(record['range_surface_area'], '')
    }
