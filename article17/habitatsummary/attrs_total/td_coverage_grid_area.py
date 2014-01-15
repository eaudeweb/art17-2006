# Script (Python)
# /article17/habitatsummary/attrs_total/td_coverage_grid_area
# params: 'record, conclusions'
## Script (Python) "td_coverage_grid_area"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, conclusions
##title=
##
return {
    'content':context.str2num(context.parse_semicolon(record['percentage_distribution_grid_area']), ''),
    'class':'center section-border',
    'title':'',
    }
