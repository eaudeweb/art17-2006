# Script (Python)
# /article17/habitatsummary/attrs_total/td_future_conclusion
# params: 'record, conclusions'
## Script (Python) "td_future_conclusion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, conclusions
##title=
##
output = context.background_colour(record['conclusion_future'], 'center', conclusions)

prospects = context.parse_semicolon(record['percentage_future']) or ''
output.update({
    'content':prospects
    })

return output
