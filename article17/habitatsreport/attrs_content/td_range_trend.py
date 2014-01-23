# Script (Python)
# /article17/habitatsreport/attrs_content/td_range_trend
# params: 'record, qa_errors'
## Script (Python) "td_range_trend"
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

#for err in qa_errors:
#    if err['FlagField'] == 'range_trend':
#        title = '%s: %s' % (err['FlagText'], err['suspect_value'])
#        class_names.append('qa_error')
#
for err in qa_errors:
    if err['FlagField'] == 'range_yearly_magnitude':
        title.append('%s: %s' % (err['FlagText'], err['suspect_value']))
        class_names.append('qa_error')
    elif record['range_yearly_magnitude'] is not None:
        title.append('Yearly magnitude = %s' % record['range_yearly_magnitude'])
        class_names.append('qa_error')

trend = record['range_trend'] or 'N/A'
return {
    'class': ' '.join(class_names),
    'title': '<br />'.join(title),
    'content': trend
    }
