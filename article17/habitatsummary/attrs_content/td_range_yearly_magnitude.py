# Script (Python)
# /article17/habitatsummary/attrs_content/td_range_yearly_magnitude
# params: 'record, qa_errors'
## Script (Python) "td_range_yearly_magnitude"
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
    if err['FlagField'] == 'range_yearly_magnitude':
        title.append('%s: %s' % (err['FlagText'], err['suspect_value']))
        class_names.append('qa_error')

return {
    'class': ' '.join(class_names),
    'title': '<br />'.join(title),
    'content': context.str2num(record['range_yearly_magnitude'])
    }
