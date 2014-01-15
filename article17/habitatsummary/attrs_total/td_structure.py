# Script (Python)
# /article17/habitatsummary/attrs_total/td_structure
# params: 'record, conclusions'
## Script (Python) "td_structure"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, conclusions
##title=
##
output = context.background_colour(record['conclusion_structure'], 'center section-border', conclusions)

conclusion = context.parse_semicolon(record['percentage_structure']) or ''
output.update({
    'content': conclusion
    })

return output
