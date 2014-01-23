# Script (Python)
# /article17/habitatsreport/attrs_content/td_grids_distribution_area
# params: 'record, qa_errors'
## Script (Python) "td_grids_distribution_area"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, qa_errors
##title=
##
class_names = ['center']
title = []

for err in qa_errors:
    if err['FlagField'] == 'distribution_grid_area':
        title.append('%s: %s' % (err['FlagText'], err['suspect_value']))
        class_names.append('qa_error')

return {
    'class': ' '.join(class_names),
    'title': '<br />'.join(title),
    'content': context.str2num(record['distribution_grid_area'])
    }
