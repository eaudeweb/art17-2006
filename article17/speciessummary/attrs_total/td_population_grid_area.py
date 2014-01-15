# Script (Python)
# /article17/speciessummary/attrs_total/td_population_grid_area
# params: 'record, conclusions'
## Script (Python) "td_population_grid_area"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, conclusions
##title=
##
return {
    'class': 'center section-border',
    'title':'',
    'content':context.str2num(context.parse_semicolon(record['percentage_distribution_grid_area']), ''),
    }
