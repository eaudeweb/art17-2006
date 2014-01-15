# Script (Python)
# /article17/habitatsummary/attrs_conclusion/td_assessment_conclusion
# params: 'habitat, region, record, conclusions'
## Script (Python) "td_assessment_conclusion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=habitat, region, record, conclusions
##title=
##
output = context.background_colour(record['conclusion_assessment'], 'center section-border', conclusions)

title = output.get('title', '')
method = record['method_assessment'] or ''

cursor = context.sql_methods.get_assesm_conclusion_value(habitatcode=habitat, region=region, assessment_method=method)

if len(cursor):
    concl_value = cursor[0]['percentage_assessment']
    if concl_value:
        title = "%s: %s" % (title, concl_value)

output.update({
    'content': method,
    'title': title,
    })

return output
