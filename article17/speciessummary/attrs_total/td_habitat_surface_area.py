# Script (Python)
# /article17/speciessummary/attrs_total/td_habitat_surface_area
# params: 'record, conclusions'
## Script (Python) "td_habitat_surface_area"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, conclusions
##title=
##
output = context.background_colour(record['conclusion_habitat'], 'center', conclusions)

output.update({
    'content':context.str2num(context.parse_semicolon(record['percentage_habitat_surface_area']), ''),
    })

return output
