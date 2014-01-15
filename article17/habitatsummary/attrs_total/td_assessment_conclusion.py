# Script (Python)
# /article17/habitatsummary/attrs_total/td_assessment_conclusion
# params: 'record, conclusions'
## Script (Python) "td_assessment_conclusion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, conclusions
##title=
##
output = context.background_colour(record['conclusion_assessment'], 'center section-border', conclusions)

conclusion = context.parse_semicolon(record['percentage_assessment']) or ''
output.update({
    'content': conclusion
    })

return output
