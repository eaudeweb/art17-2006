# Script (Python)
# /article17/speciessummary/attrs_total/td_population_conclusion
# params: 'record, conclusions'
## Script (Python) "td_population_conclusion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, conclusions
##title=
##
output = context.background_colour(record['conclusion_population'], 'center', conclusions)

output.update({
    'content':context.str2num(context.parse_semicolon(record['percentage_population_mean_size']), ''),
    })

return output
