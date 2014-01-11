# Script (Python)
# /article17/speciessummary/attrs_content/td_range_conclusion
# params: 'record, conclusions, qa_errors'
## Script (Python) "td_range_conclusion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, conclusions, qa_errors
##title=
##
output = context.background_colour(record['conclusion_range'], 'center', conclusions)

class_names = [output['class']]
title = [output['title']]

for err in qa_errors:
    if err['FlagField'] in ['conclusion_range', 'percentage_range_surface_area']:
        title.append('%s: %s' % (err['FlagText'], err['suspect_value']))
        class_names.append('qa_error')

output.update({
    'content':context.str2num(record['percentage_range_surface_area']),
    'title': '<br />'.join(title),
    'class': ' '.join(class_names),
    })

return output
