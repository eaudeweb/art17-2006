# Script (Python)
# /article17/speciessummary/attrs_total/td_habitat_grid_area
# params: 'record, conclusions'
## Script (Python) "td_habitat_grid_area"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, conclusions
##title=
##
output = context.background_colour(record['conclusion_habitat_gis'], 'center', conclusions)

output.update({
    'content':context.str2num(context.parse_semicolon(record['percentage_distribution_grid_area']), ''),
    })

return output
