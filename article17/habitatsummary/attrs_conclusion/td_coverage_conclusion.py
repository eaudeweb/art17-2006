# Script (Python)
# /article17/habitatsummary/attrs_conclusion/td_coverage_conclusion
# params: 'habitat, region, record, conclusions'
## Script (Python) "td_coverage_conclusion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=habitat, region, record, conclusions
##title=
##
output = context.background_colour(record['conclusion_area'], 'center', conclusions)

title = output.get('title', '')
method = record['method_area'] or ''

cursor = context.sql_methods.get_coverage_conclusion_value(habitatcode=habitat, region=region, assessment_method=method)

if len(cursor):
    concl_value = cursor[0]['percentage_coverage_surface_area']
    if concl_value:
        title = "%s: %s" % (title, concl_value)

output.update({
    'content': method,
    'title': title,
    })

return output
