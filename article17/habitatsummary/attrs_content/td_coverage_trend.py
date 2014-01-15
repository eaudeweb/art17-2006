# Script (Python)
# /article17/habitatsummary/attrs_content/td_coverage_trend
# params: 'record, qa_errors'
## Script (Python) "td_coverage_trend"
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
#    if err['FlagField'] == 'coverage_trend':
#        title = '%s: %s' % (err['FlagText'], err['suspect_value'])
#        class_names.append('qa_error')

for err in qa_errors:
    if err['FlagField'] == 'coverage_yearly_magnitude':
        title.append('%s: %s' % (err['FlagText'], err['suspect_value']))
        class_names.append('qa_error')
    elif record['coverage_yearly_magnitude'] is not None:
        title.append('Yearly magnitude = %s' % record['coverage_yearly_magnitude'])
        class_names.append('qa_error')

trend = record['coverage_trend'] or 'N/A'
return {
    'class': ' '.join(class_names),
    'title': '<br />'.join(title),
    'content': trend
    }
