# Script (Python)
# /article17/speciessummary/attrs_total/td_range_grid_area
# params: 'record, conclusions'
## Script (Python) "td_range_grid_area"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, conclusions
##title=
##
return {
    'class': 'center',
    'title':'',
    'content':context.str2num(context.parse_semicolon(record['percentage_range_grid_area']), ''),
    }
