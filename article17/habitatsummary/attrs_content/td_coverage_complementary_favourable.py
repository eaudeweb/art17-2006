# Script (Python)
# /article17/habitatsummary/attrs_content/td_coverage_complementary_favourable
# params: 'record, qa_errors'
## Script (Python) "td_coverage_complementary_favourable"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, qa_errors
##title=
##
class_names = ['number', 'section-border']
title = []
range_q = record['complementary_favourable_area_q'] or ''
range = record['complementary_favourable_area']

for err in qa_errors:
    if err['FlagField'] == ['complementary_favourable_area_q', 'complementary_favourable_area']:
        title.append('%s: %s' % (err['FlagText'], err['suspect_value']))
        class_names.append('qa_error')

if range_q or range:
    content = '%s%s' % (range_q, context.str2num(range, ''))
else:
    content = 'N/A'

return {
    'class': ' '.join(class_names),
    'title': '<br />'.join(title),
    'content': content
    }
