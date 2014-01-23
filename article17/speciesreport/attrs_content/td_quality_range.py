# Script (Python)
# /article17/speciesreport/attrs_content/td_quality_range
# params: 'record, qa_errors'
## Script (Python) "td_quality_range"
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

quality = record['range_quality'] or 'N/A'
if quality.startswith('M'):
    title.append('Moderate')
elif quality.startswith('G'):
    title.append('Good')
elif quality.startswith('P'):
    title.append('Poor')

for err in qa_errors:
    if err['FlagField'] == 'range_quality':
        title.append('%s: %s' % (err['FlagText'], err['suspect_value']))
        class_names.append('qa_error')

return {
    'class': ' '.join(class_names),
    'title': '<br />'.join(title),
    'content': quality
    }
