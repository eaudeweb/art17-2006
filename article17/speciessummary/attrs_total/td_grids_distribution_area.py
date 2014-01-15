# Script (Python)
# /article17/speciessummary/attrs_total/td_grids_distribution_area
# params: 'record'
## Script (Python) "td_grids_distribution_area"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record
##title=
##
distribution = context.parse_semicolon(record['distribution_grid_area'])
return {
    'class': 'center',
    'content': context.str2num(distribution, '')
    }
