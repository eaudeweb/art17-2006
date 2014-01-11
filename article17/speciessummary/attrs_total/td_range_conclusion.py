# Script (Python)
# /article17/speciessummary/attrs_total/td_range_conclusion
# params: 'record, conclusions'
## Script (Python) "td_range_conclusion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, conclusions
##title=
##
output = context.background_colour(record['conclusion_range'], 'center', conclusions)

output.update({
    'content':context.str2num(context.parse_semicolon(record['percentage_range_surface_area']), ''),
    })

return output
