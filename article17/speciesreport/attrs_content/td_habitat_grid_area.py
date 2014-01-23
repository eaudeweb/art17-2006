# Script (Python)
# /article17/speciesreport/attrs_content/td_habitat_grid_area
# params: 'record, conclusions, qa_errors'
## Script (Python) "td_habitat_grid_area"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, conclusions, qa_errors
##title=
##
output = context.background_colour(record['conclusion_habitat'], 'center', conclusions)

class_names = [output['class']]
title = [output['title']]

for err in qa_errors:
    if err['FlagField'] in ['conclusion_habitat', 'percentage_distribution_grid_area']:
        title.append('%s: %s' % (err['FlagText'], err['suspect_value']))
        class_names.append('qa_error')


output.update({
    'content':context.str2num(record['percentage_distribution_grid_area']),
    'title': '<br />'.join(title),
    'class': ' '.join(class_names),
    })

return output
