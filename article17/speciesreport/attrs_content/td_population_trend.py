# Script (Python)
# /article17/speciesreport/attrs_content/td_population_trend
# params: 'record, qa_errors'
## Script (Python) "td_population_trend"
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
trend = record['population_trend'] or 'N/A'

#for err in qa_errors:
#    if err['FlagField'] == 'population_trend':
#        title = '%s: %s' % (err['FlagText'], err['suspect_value'])
#        class_names.append('qa_error')

for err in qa_errors:
    if err['FlagField'] == 'population_yearly_magnitude':
        title.append('%s: %s' % (err['FlagText'], err['suspect_value']))
        class_names.append('qa_error')
    elif record['population_yearly_magnitude'] is not None:
        title.append('Yearly magnitude = %s' % record['population_yearly_magnitude'])
        class_names.append('qa_error')

return {
    'class': ' '.join(class_names),
    'title': '<br />'.join(title),
    'content': trend
    }
