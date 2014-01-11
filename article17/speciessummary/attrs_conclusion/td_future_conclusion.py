# Script (Python)
# /article17/speciessummary/attrs_conclusion/td_future_conclusion
# params: 'assesment_speciesname, region, record, conclusions'
## Script (Python) "td_future_conclusion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=assesment_speciesname, region, record, conclusions
##title=
##
output = context.background_colour(record['conclusion_future'], 'center section-border', conclusions)

title = output.get('title', '')
method = record['method_future'] or ''

cursor = context.sql_methods.get_future_conclusion_value(assesment_speciesname=assesment_speciesname, region=region, assessment_method=method)

if len(cursor):
    concl_value = cursor[0]['percentage_future']
    if concl_value:
        title = "%s: %s" % (title, concl_value)

output.update({
    'content': method,
    'title': title,
    })

return output
