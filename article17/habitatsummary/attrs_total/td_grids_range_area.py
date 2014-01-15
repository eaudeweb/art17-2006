# Script (Python)
# /article17/habitatsummary/attrs_total/td_grids_range_area
# params: 'record'
## Script (Python) "td_grids_range_area"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record
##title=
##
range = context.parse_semicolon(record['range_grid_area'])
return {
    'class': 'center',
    'content': context.str2num(range, '')
    }
