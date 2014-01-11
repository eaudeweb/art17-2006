# Script (Python)
# /article17/speciessummary/attrs_content/td_habitat_trend
# params: 'record, qa_errors'
## Script (Python) "td_habitat_trend"
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
trend = record['habitat_trend'] or 'N/A'

for err in qa_errors:
    if err['FlagField'] == 'habitat_trend':
        title.append('%s: %s' % (err['FlagText'], err['suspect_value']))
        class_names.append('qa_error')

return {
    'class': ' '.join(class_names),
    'title': '<br />'.join(title),
    'content': trend
    }
