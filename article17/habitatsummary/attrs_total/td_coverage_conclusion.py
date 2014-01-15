# Script (Python)
# /article17/habitatsummary/attrs_total/td_coverage_conclusion
# params: 'record, conclusions'
## Script (Python) "td_coverage_conclusion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, conclusions
##title=
##
output = context.background_colour(record['conclusion_coverage'], 'center', conclusions)

output.update({
    'content':context.str2num(context.parse_semicolon(record['percentage_coverage_surface_area']), ''),
    })

return output
