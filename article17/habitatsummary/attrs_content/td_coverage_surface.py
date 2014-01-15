# Script (Python)
# /article17/habitatsummary/attrs_content/td_coverage_surface
# params: 'record, qa_errors'
## Script (Python) "td_coverage_surface"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, qa_errors
##title=
##
class_names = ['number']
title = []

for err in qa_errors:
    if err['FlagField'] == 'coverage_surface_area':
        title.append('%s: %s' % (err['FlagText'], err['suspect_value']))
        class_names.append('qa_error')

return {
    'class': ' '.join(class_names),
    'title': '<br />'.join(title),
    'content': context.str2num(record['coverage_surface_area'])
    }
